#!/usr/bin/env python3

import json
import os
from .workout import Workout

class WorkoutManager:

    def __init__(self, data_file="workouts.json"):
        self.workouts = []
        self.data_file = data_file
        self.load_workouts()

    def add_workout(self, workout_name, category, duration, customer_name, starting_time):
        self.load_workouts()
        self.workouts.append(Workout(workout_name, duration, category, customer_name, starting_time))
        self.save_workouts()

    def get_all_workouts(self):
        return self.workouts

    def save_workouts(self):
        try:
            with open(self.data_file, 'w') as f:
                json.dump([workout.to_dict() for workout in self.workouts], f, indent=4)
            return True
        except Exception as e:
            print(f"Error saving workouts: {e}")
            return False

    def load_workouts(self):
        self.workouts = []
        if not os.path.exists(self.data_file):
            try:
                os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
                with open(self.data_file, 'w') as f:
                    json.dump([], f)
                return True
            except Exception as e:
                print(f"Error creating workout file: {e}")
                return False

        try:
            with open(self.data_file, 'r') as f:
                data = f.read()
                if not data.strip():
                    self.workouts = []
                    return True
                    
                workout_dicts = json.loads(data)

                if not isinstance(workout_dicts, list):
                    return False

                for wd in workout_dicts:
                    try:
                        workout = Workout.from_dict(wd)
                        self.workouts.append(workout)
                    except (KeyError, TypeError) as e:
                        print(f"Skipping invalid workout entry due to missing key or wrong type: {e} in {wd}")
                return True
        except json.JSONDecodeError:
            print(f"{self.data_file} contains invalid JSON. Initializing with empty workout list.")
            return False
        except Exception as e:
            print(f"Error loading workouts: {e}")
            return False

    def get_total_workout_time(self):
        return sum(workout.duration for workout in self.workouts)

    def get_average_workout_time(self):
        if not self.workouts:
            return 0
        return self.get_total_workout_time() / len(self.workouts)

    def get_workout_stats(self):
        if not self.workouts:
            return {
                "total_workouts": 0,
                "total_time": 0,
                "average_time": 0,
                "most_common_workout": "None",
                "category_breakdown": {},
                "most_common_category": "None"
            }

        workout_counts = {}
        category_counts = {}
        
        for workout in self.workouts:
            name = workout.workout_name
            category = workout.category
            workout_counts[name] = workout_counts.get(name, 0) + 1
            category_counts[category] = category_counts.get(category, 0) + 1

        most_common_workout = max(workout_counts.items(), key=lambda x: x[1])[0] if workout_counts else "None"
        most_common_category = max(category_counts.items(), key=lambda x: x[1])[0] if category_counts else "None"

        return {
            "total_workouts": len(self.workouts),
            "total_time": self.get_total_workout_time(),
            "average_time": round(self.get_average_workout_time(), 1),
            "most_common_workout": most_common_workout,
            "category_breakdown": category_counts,
            "most_common_category": most_common_category
        }

    def delete_workouts(self, workout_ids):
        self.load_workouts()
        self.workouts = [workout for workout in self.workouts if str(workout.id) not in workout_ids]
        self.save_workouts()