FROM python:3.11-slim

WORKDIR /app

# Avoid python buffering + speed
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system deps (optional but safer for production)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (cache optimization)
COPY backend/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY backend/ .

# Cloud Run uses 8080
EXPOSE 8080

# Start FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]