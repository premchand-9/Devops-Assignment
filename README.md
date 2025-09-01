# ACEestFitness and Gym Tracker

A simple fitness tracking application built with Python and Flask that allows users to log and view their workout activities.

## Features

- Add workouts with duration
- View logged workout history
- Delete workouts
- View Statistics

## Installation

### Prerequisites

- Python 3.9
- pip (Python package installer)

### Setup

1. Clone the repository or download the source code

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Running the Application

Run the application using Python:

```bash
python run_app.py
```

### Running with Docker

1. Build the Docker image:

```bash
docker build -t fitness-tracker .
```

2. Run the Docker container:

```bash
docker run -p 5000:5000 fitness-tracker
```

Alternatively, we can use Docker Compose:

```bash
docker-compose up --build
```

### How to Use

1. Enter the name of your workout in the "Workout" field
2. Enter the duration in minutes in the "Duration" field
3. Click "Add Workout" to save your workout
4. Click "Workouts History" to see all logged workouts
5. Click "Statistics" to see statistics about your workouts
6. Click "Delete" to delete a workout

## Project Structure

```
.
├── .dockerignore       # Docker ignore file
├── .github/            # GitHub Actions workflows
│   └── workflows/
│       └── main.yml    # CI/CD workflow (build and test)
├── .gitignore          # Git ignore file
├── Dockerfile          # Docker build file
├── README.md           # Project documentation
├── data/               # Data directory
│   └── workouts.json   # Stores workout data
├── docker-compose.yml  # Docker Compose configuration
├── requirements.txt    # Python dependencies
├── run_app.py          # Script to run the Flask application
├── run_tests.py        # Script to run tests
├── src/                # Source code directory
│   ├── app_web.py      # Main Flask application
│   └── models/         # Data models
│       ├── workout.py  # Workout data model
│       └── workout_manager.py # Manages workout data
├── static/             # Static files (CSS, JS, images)
│   └── style.css       # Application stylesheet
└── templates/          # HTML templates
    └── index.html      # Main application HTML template
└── tests/              # Test directory
    ├── test_workout.py # Tests for the Workout model
    └── test_workout_manager.py # Tests for the WorkoutManager model
```

## Development

### Running Tests

To run the unit tests for the application:

```bash
python run_tests.py
```

### Running Tests with Docker

To run the unit tests within the Docker container:

```bash
docker-compose up -d
docker-compose exec app python -m pytest
docker-compose down
```