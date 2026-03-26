FROM python:3.13-slim

WORKDIR /app

# Install dependencies first (layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create non-root user
RUN adduser --disabled-password --gecos "" appuser && \
    chown -R appuser:appuser /app

# Copy application code
COPY . .

USER appuser
ENV PATH="/home/appuser/.local/bin:$PATH"

# Cloud Run sets PORT; default to 8080
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port $PORT"]
