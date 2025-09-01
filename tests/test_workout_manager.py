import unittest
import os
import json
from src.models.workout_manager import WorkoutManager
from src.models.workout import Workout

class TestWorkoutManager(unittest.TestCase):
    def setUp(self):
        self.test_data_file = 'data/test_workouts.json'
        self.manager = WorkoutManager(self.test_data_file)
        if os.path.exists(self.test_data_file):
            os.remove(self.test_data_file)
        with open(self.test_data_file, 'w') as f:
            json.dump([], f)

    def tearDown(self):
        if os.path.exists(self.test_data_file):
            os.remove(self.test_data_file)

    def test_add_workout(self):
        workout = Workout("Running", 30, "Cardio", "John Doe", "08:00")
        self.manager.add_workout(workout.workout_name, workout.category, workout.duration, workout.customer_name, workout.starting_time)
        workouts = self.manager.get_all_workouts()
        self.assertEqual(len(workouts), 1)
        self.assertEqual(workouts[0].workout_name, "Running")

    def test_get_all_workouts(self):
        workout1 = Workout("Running", 30, "Cardio", "John Doe", "08:00")
        workout2 = Workout("Weightlifting", 60, "Strength", "Jane Smith", "10:00")
        self.manager.add_workout(workout1.workout_name, workout1.category, workout1.duration, workout1.customer_name, workout1.starting_time)
        self.manager.add_workout(workout2.workout_name, workout2.category, workout2.duration, workout2.customer_name, workout2.starting_time)
        workouts = self.manager.get_all_workouts()
        self.assertEqual(len(workouts), 2)

    def test_delete_workouts(self):
        workout1 = Workout("Running", 30, "Cardio", "John Doe", "08:00")
        workout2 = Workout("Weightlifting", 60, "Strength", "Jane Smith", "10:00")
        self.manager.add_workout(workout1.workout_name, workout1.category, workout1.duration, workout1.customer_name, workout1.starting_time)
        self.manager.add_workout(workout2.workout_name, workout2.category, workout2.duration, workout2.customer_name, workout2.starting_time)
        workouts = self.manager.get_all_workouts()
        ids_to_delete = [workouts[0].id]
        self.manager.delete_workouts(ids_to_delete)
        remaining_workouts = self.manager.get_all_workouts()
        self.assertEqual(len(remaining_workouts), 1)
        self.assertEqual(remaining_workouts[0].workout_name, "Weightlifting")

    def test_get_workout_stats_no_workouts(self):
        stats = self.manager.get_workout_stats()
        self.assertEqual(stats["total_time"], 0)
        self.assertEqual(stats["average_time"], 0)
        self.assertEqual(stats["most_common_workout"], "None")
        self.assertEqual(stats["most_common_category"], "None")
        self.assertEqual(stats["category_breakdown"], {})

    def test_get_workout_stats_with_workouts(self):
        workout1 = Workout("Running", 30, "Cardio", "John Doe", "08:00")
        workout2 = Workout("Weightlifting", 60, "Strength", "Jane Smith", "10:00")
        workout3 = Workout("Running", 45, "Cardio", "Peter Jones", "12:00")
        self.manager.add_workout(workout1.workout_name, workout1.category, workout1.duration, workout1.customer_name, workout1.starting_time)
        self.manager.add_workout(workout2.workout_name, workout2.category, workout2.duration, workout2.customer_name, workout2.starting_time)
        self.manager.add_workout(workout3.workout_name, workout3.category, workout3.duration, workout3.customer_name, workout3.starting_time)

        stats = self.manager.get_workout_stats()
        self.assertEqual(stats["total_time"], 135)
        self.assertAlmostEqual(stats["average_time"], 45.0)
        self.assertEqual(stats["most_common_workout"], "Running")
        self.assertEqual(stats["most_common_category"], "Cardio")
        self.assertEqual(stats["category_breakdown"], {"Cardio": 2, "Strength": 1})

if __name__ == '__main__':
    unittest.main()