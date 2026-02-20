from fastapi.testclient import TestClient
from module3.milestone2.app.app import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_predict_success():
    r = client.post("/predict", json={"features": [1, 2, 3]})
    assert r.status_code == 200
    body = r.json()
    assert "prediction" in body
    assert isinstance(body["prediction"], float)

def test_predict_missing_features():
    r = client.post("/predict", json={})
    assert r.status_code in (400, 422)

def test_predict_empty_features():
    r = client.post("/predict", json={"features": []})
    assert r.status_code in (400, 422)
