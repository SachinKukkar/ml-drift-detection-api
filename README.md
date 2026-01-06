# ML Drift Detection API

An end-to-end machine learning inference service with real-time data drift detection, built using FastAPI and Evidently, and fully containerized with Docker.

## Overview
This project demonstrates how a machine learning model can be deployed as a production-ready API while continuously monitoring incoming data for distribution shifts (data drift). In addition to serving predictions, the system evaluates whether new input data deviates significantly from the training data, which is a critical aspect of maintaining reliable ML systems in real-world deployments.

## Features
- Machine learning model training and inference
- REST API for real-time predictions
- Automated data drift detection using Evidently
- Clean, modular project structure
- Fully Dockerized for reproducible deployment

## Tech Stack
- Python
- scikit-learn
- FastAPI
- Evidently AI
- Docker

## Project Structure
ml-drift-detection-api/
├── app/ # FastAPI application
├── data/ # Reference training data
├── model/ # Model training and saved artifacts
├── drift/ # Data drift detection logic
├── Dockerfile
├── requirements.txt
├── README.md
└── .gitignore





## How It Works
1. A RandomForest classifier is trained on a structured tabular dataset.
2. The training dataset is stored as reference data for drift comparison.
3. Incoming requests sent to the API are passed to the trained model for prediction.
4. The incoming data is compared against the reference dataset using Evidently to detect data drift.
5. The API returns both the prediction result and drift metrics indicating whether drift is detected.

## API Usage
The application exposes a `/predict` endpoint that accepts a list of numerical feature values and returns the model prediction along with data drift information.

Example request:
```json
{
  "features": [30 numerical feature values]
}

```

Example response:
```
{
  "prediction": 0,
  "drift": {
    "drift_detected": false,
    "drift_score": 0.0
  }
}
```

Runnning Locally 
Create and activate a virtual environment.

Install dependencies:
pip install -r requirements.txt

Start the API server : 
uvicorn app.main:app --reload

Open the swagger UI at : 
http://127.0.0.1:8000/docs

Running with Docker

build and run the Docker container using the following commands : 
docker build -t ml-drift-api .
docker run -p 8000:8000 ml-drift-api
