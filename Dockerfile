FROM python:3.12-slim
WORKDIR /app
# Install packages directly (bypass requirements.txt)
RUN pip install --no-cache-dir google-adk aiosqlite "uvicorn[standard]"
# Verify installation
RUN pip list | grep -i google-adk
RUN python -c "from google.adk.cli.fast_api import get_fast_api_app; print('ADK OK')"
# Copy app code and clean up
COPY . .
RUN rm -rf .venv __pycache__ .git .env
RUN adduser --disabled-password --gecos "" appuser && \
    chown -R appuser:appuser /app
USER appuser
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port $PORT"]
