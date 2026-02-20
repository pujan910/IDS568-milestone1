# IDS 568 – Milestone 2
## Dockerized FastAPI Application with Tests

### Overview
This milestone containerizes a FastAPI application using Docker and Docker Compose.  
The application exposes two endpoints:

- GET /health → Health check
- POST /predict → Returns model prediction

---

## 🔹 Run Locally (Without Docker)

From project root:

python -m pytest module3/milestone2/tests -q
---

## 🔹 Build Docker Image

From inside module3/milestone2:

docker build -t milestone2-app .
---

## 🔹 Run with Docker Compose

docker compose up --build
App runs at:

http://localhost:8080
---

## 🔹 Test Endpoints

Health check:

curl http://127.0.0.1:8080/health
Prediction:

curl -X POST http://127.0.0.1:8080/predict

-H "Content-Type: application/json"
-d '{"features":[1,2,3]}'
---

## 🔹 Stop Container

docker compose down
---

## 🔹 Run Tests Inside Container

docker compose exec app python -m pytest -q
