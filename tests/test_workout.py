import unittest
from src.models.workout import Workout

class TestWorkout(unittest.TestCase):
    def test_workout_creation(self):
        workout = Workout("Running", 30, "Cardio", "John Doe", "08:00")
        self.assertEqual(workout.workout_name, "Running")
        self.assertEqual(workout.duration, 30)
        self.assertEqual(workout.category, "Cardio")

    def test_workout_to_dict(self):
        workout = Workout("Weightlifting", 60, "Strength", "Jane Smith", "10:00")
        expected_dict = {
            "workout": "Weightlifting",
            "duration": 60,
            "category": "Strength",
            "customer_name": "Jane Smith",
            "starting_time": "10:00",
            "date": workout.date,
            "id": workout.id
        }
        self.assertEqual(workout.to_dict(), expected_dict)

    def test_workout_from_dict(self):
        workout_dict = {
            "workout": "Yoga",
            "duration": 45,
            "category": "Flexibility"
        }
        workout = Workout.from_dict(workout_dict)
        self.assertEqual(workout.workout_name, "Yoga")
        self.assertEqual(workout.duration, 45)
        self.assertEqual(workout.category, "Flexibility")

if __name__ == '__main__':
    unittest.main()