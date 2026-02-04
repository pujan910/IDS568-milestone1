# IDS568-milestone1

IDS 568 Milestone 1 – Model serving with FastAPI, Cloud Run, and Cloud Functions

---

## Overview

This project demonstrates an end-to-end machine learning deployment pipeline using FastAPI, Docker, and Google Cloud services.  
A trained machine learning model is exposed as a REST API that accepts input features and returns predictions.  
The model is deployed using both **Google Cloud Run** and **Google Cloud Functions**.

---

## Tech Stack

- Python  
- FastAPI  
- Docker  
- Google Cloud Run  
- Google Cloud Functions  
- Google Artifact Registry  
- Google Cloud Build  

---

## Project Structure
IDS568-milestone1/
├── Dockerfile
├── main.py
├── model.pkl
├── requirements.txt
├── cloud_function/
│ ├── main.py
│ └── requirements.txt
└── README.md


## Deployed Services

### Cloud Run (FastAPI Service)

**Base URL:**  
https://fastapi-service-226183649533.us-central1.run.app

**Swagger UI:**  
https://fastapi-service-226183649533.us-central1.run.app/docs

> Note: Accessing the base URL directly in a browser returns `{"detail":"Not Found"}`.  
> This is expected behavior because the API only exposes the `/predict` endpoint.

**Example request:**
```bash
curl -X POST "https://fastapi-service-226183649533.us-central1.run.app/predict" \
  -H "Content-Type: application/json" \
  -d '{"features":[5.1,3.5,1.4,0.2]}'

  ## AFTER RUNNING IT, OUR PREDICTED RESPONSE WAS:
  {"prediction": 0}


## Summary

This milestone demonstrates successful model serving using both Cloud Run and Cloud Functions.  
The deployed services accept numerical feature inputs and return predictions through a REST API interface.
