from fastapi import FastAPI, HTTPException
import pickle
import os

from schema import ChurnInput
from utils import preprocess_input

import pandas as pd

app = FastAPI(title="Churn Prediction API")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model_path = os.path.join(BASE_DIR, "Model", "model.pkl")
scaler_path = os.path.join(BASE_DIR, "Model", "scaler.pkl")

model = pickle.load(open(model_path, "rb"))
scaler = pickle.load(open(scaler_path, "rb"))


@app.get("/")
def home():
    return {"message": "Churn Prediction API is running"}


@app.post("/predict")
def predict(data: ChurnInput):
    try:
        input_df = preprocess_input(data)

        scale_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']
        input_df[scale_cols] = scaler.transform(input_df[scale_cols])

        churn_prob = model.predict_proba(input_df)[0][1]

        if churn_prob < 0.4:
            risk = "Low Risk"
        elif churn_prob < 0.7:
            risk = "Moderate Risk"
        else:
            risk = "High Risk"

        return {
            "churn_probability": round(float(churn_prob), 4),
            "risk_level": risk
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))