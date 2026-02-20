
# =========================
# Builder stage
# =========================
FROM python:3.11-slim AS builder
WORKDIR /app

COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# =========================
# Runtime stage
# =========================
FROM python:3.11-slim
WORKDIR /app

# Copy installed site-packages from builder
COPY --from=builder /usr/local /usr/local

# Copy service code
COPY app/ /app/app/

# Create non-root user
RUN useradd -m appuser
USER appuser

EXPOSE 8080
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8080"]
