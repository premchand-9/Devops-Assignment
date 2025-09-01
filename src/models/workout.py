#!/usr/bin/env python3

from datetime import datetime
import uuid

class Workout:

    def __init__(self, workout_name, duration, category, customer_name, starting_time):
        self.workout_name = workout_name
        self.duration = duration
        self.category = category
        self.customer_name = customer_name
        self.starting_time = starting_time
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.id = str(uuid.uuid4())

    def to_dict(self):
        return {
            "workout": self.workout_name,
            "duration": self.duration,
            "category": self.category,
            "customer_name": self.customer_name,
            "starting_time": self.starting_time,
            "date": self.date,
            "id": self.id
        }

    @classmethod
    def from_dict(cls, workout_dict):
        workout = cls(
            workout_name=workout_dict["workout"],
            duration=workout_dict["duration"],
            category=workout_dict.get("category"),
            customer_name=workout_dict.get("customer_name"),
            starting_time=workout_dict.get("starting_time")
        )
        workout.id = workout_dict.get("id")
        workout.date = workout_dict.get("date")
        return workout