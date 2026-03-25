FROM python:3.12-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY ./edem_api ./edem_api

ENV PORT=8000

# Start FastAPI
CMD ["uvicorn", "edem_api.main:app", "--host", "0.0.0.0", "--port", "8000"]