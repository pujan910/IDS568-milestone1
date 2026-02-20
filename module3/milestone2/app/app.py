from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, conlist
import joblib
import os

app = FastAPI(title="Milestone 2 ML Service")

MODEL_PATH = os.getenv("MODEL_PATH", "app/model.joblib")

class PredictRequest(BaseModel):
    features: conlist(float, min_length=1)

class PredictResponse(BaseModel):
    prediction: float

def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model not found at {MODEL_PATH}")
    return joblib.load(MODEL_PATH)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    try:
        model = load_model()
        y = model.predict([req.features])[0]
        return {"prediction": float(y)}
    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Inference failed: {e}")

