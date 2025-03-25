<<<<<<< HEAD
# Disease_Detection
=======
# Disease Prediction System

A web application that uses machine learning to predict diseases based on symptoms.

## Overview

This project uses multiple machine learning models (SVM, Naive Bayes, and Random Forest) to predict diseases based on the symptoms provided by the user. The final prediction is determined by taking the majority vote from all three models.

## Features

- Interactive web interface for selecting symptoms
- Search functionality for easy symptom selection
- Predictions from multiple machine learning models
- Responsive design for all devices

## Setup and Installation

1. Clone this repository
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the Flask application:
   ```
   python app.py
   ```
4. Open your browser and navigate to `http://127.0.0.1:5000/`

## Project Structure

- `app.py`: The main Flask application
- `disease_prediction_system.pkl`: Pre-trained machine learning models
- `templates/`: HTML templates for the web interface
- `static/`: CSS and JavaScript files for styling and interactivity
- `Training.csv` and `Testing.csv`: Datasets used for training and testing the models

## How It Works

1. The user selects symptoms from the provided list
2. The application preprocesses the input data
3. The data is passed to three different machine learning models
4. Each model makes a prediction
5. The final prediction is determined by majority voting
6. The results are displayed to the user

## Disclaimer

This application is for educational purposes only and should not replace professional medical advice. Always consult with a healthcare professional for proper diagnosis and treatment. 
>>>>>>> 447a4c6 (initial commit)
