from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

from drift.drift_check import check_drift

app = FastAPI(title="ML Drift Detection API")

# Load model & reference data
model = joblib.load("model/model.pkl")
reference_df = pd.read_csv("data/train.csv").drop(columns=["target"])

class InputData(BaseModel):
    features: list[float]

@app.post("/predict")
def predict(data: InputData):
    X = pd.DataFrame([data.features], columns=reference_df.columns)

    # Prediction
    prediction = model.predict(X)[0]

    # Drift check
    drift_result = check_drift(reference_df, X)

    return {
        "prediction": int(prediction),
        "drift": drift_result
    }
