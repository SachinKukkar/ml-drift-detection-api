🚀 ML Drift Detection API

An end-to-end Machine Learning inference service with real-time data drift detection, built using FastAPI and Evidently AI, and fully containerized with Docker.

This project demonstrates how to deploy an ML model as a production-ready API while continuously monitoring incoming data for distribution shifts (data drift)—a critical requirement for reliable real-world ML systems.

📌 Overview

In real production environments, model performance can degrade over time due to changes in incoming data. This project solves that problem by:

Serving predictions through a REST API

Continuously comparing live input data with training data

Detecting and reporting data drift in real time

Along with predictions, the API returns drift metrics, enabling proactive monitoring and maintenance of ML models.

✨ Key Features

🔹 Machine learning model training & inference

🔹 RESTful API using FastAPI

🔹 Automated data drift detection using Evidently

🔹 Modular and scalable project structure

🔹 Fully Dockerized for reproducible deployment

🧠 Tech Stack

Python

scikit-learn

FastAPI

Evidently AI

Docker

📁 Project Structure
ml-drift-detection-api/
│
├── app/            # FastAPI application (API routes & schemas)
├── data/           # Reference training data
├── model/          # Model training & saved artifacts
├── drift/          # Data drift detection logic
│
├── Dockerfile
├── requirements.txt
├── README.md
└── .gitignore

⚙️ How It Works

A RandomForest classifier is trained on a structured tabular dataset.

The training dataset is saved as reference data for drift detection.

Incoming API requests are passed to the trained model for prediction.

Input data is compared against reference data using Evidently.

The API returns:

Model prediction

Drift detection status

Drift score

🔌 API Usage
Endpoint
POST /predict

Example Request
{
  "features": [30 numerical feature values]
}

Example Response
{
  "prediction": 0,
  "drift": {
    "drift_detected": false,
    "drift_score": 0.0
  }
}

🧪 Run Locally
1️⃣ Create & activate a virtual environment
python -m venv venv
source venv/bin/activate

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Start the API server
uvicorn app.main:app --reload

4️⃣ Open Swagger UI
http://127.0.0.1:8000/docs

🐳 Run with Docker
Build the Docker image
docker build -t ml-drift-api .

Run the container
docker run -p 8000:8000 ml-drift-api

Access the API
http://localhost:8000/docs

🎯 Use Cases

Monitoring ML models in production

Detecting data distribution shifts

Building reliable MLOps pipelines

Learning production-grade ML deployment

📌 Future Improvements

Add model performance monitoring

Store drift metrics in a database

Add alerting (Slack / Email)

Support batch predictions

📄 License

This project is open-source and intended for learning, experimentation, and production demos.
