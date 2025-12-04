FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy API + emulator files
COPY api.py emulator.py telemetry_emulator.json ./

EXPOSE 8000

# Start FastAPI + emulator in same container:
# - uvicorn serves the API
# - emulator continuously posts telemetry to it
CMD ["sh", "-c", "uvicorn api:app --host 0.0.0.0 --port 8000 & python emulator.py"]
