import json
import joblib
import numpy as np

# Load model once (cold start)
model = joblib.load("model.pkl")

def predict(request):
    data = request.get_json(silent=True)
    if not data or "features" not in data:
        return (json.dumps({"error": "Missing 'features' in request body"}), 400, {"Content-Type": "application/json"})

    features = np.array(data["features"]).reshape(1, -1)
    pred = int(model.predict(features)[0])

    return (json.dumps({"prediction": pred}), 200, {"Content-Type": "application/json"})

