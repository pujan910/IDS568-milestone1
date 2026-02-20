import pickle
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

# Load model ONCE at startup (important for grading)
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI(title="IDS 568 Milestone 1 API")

# Request schema
class PredictRequest(BaseModel):
    features: List[float]

# Response schema
class PredictResponse(BaseModel):
    prediction: int

@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest):
    prediction = model.predict([request.features])[0]
    return PredictResponse(prediction=int(prediction))
