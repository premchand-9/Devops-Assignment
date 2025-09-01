from src.models.workout_manager import WorkoutManager
from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__, template_folder='../templates', static_folder=os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static')))
workout_manager = WorkoutManager('data/workouts.json')
workout_manager.load_workouts()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/workouts', methods=['GET'])
def get_workouts():
    workouts = workout_manager.get_all_workouts()
    return jsonify([w.to_dict() for w in workouts])

@app.route('/add_workout', methods=['POST'])
def add_workout():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400
    try:
        customer_name = data['customer_name']
        workout_name = data['workout_name']
        category = data['category']
        duration = int(data['duration'])
        starting_time = int(data['starting_time'])
        workout_manager.add_workout(workout_name, category, duration, customer_name, starting_time)
        return jsonify({"status": "success", "message": "Workout added successfully"}), 201
    except KeyError as e:
        print(f"Missing data: {e}")
        return jsonify({"error": f"Missing data: {e}"}), 400
    except ValueError as e:
        print(f"Invalid data type: {e}")
        return jsonify({"error": f"Invalid data type: {e}"}), 400

@app.route('/stats', methods=['GET'])
def get_stats():
    return workout_manager.get_workout_stats()

@app.route('/delete_workouts', methods=['POST'])
def delete_workouts():
    data = request.get_json()
    if not data or 'workout_ids' not in data:
        return jsonify({"error": "Invalid request"}), 400
    try:
        workout_ids = data['workout_ids']
        workout_manager.delete_workouts(workout_ids)
        return jsonify({"status": "success", "message": "Workouts deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500