FROM python:3.11-slim

WORKDIR /app

# Install dependencies separately for better caching
COPY . .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi

# Copy only the source code
COPY src/ ./src

# Expose the FastAPI port
EXPOSE 8000

CMD ["uvicorn", "src.user_service.main:app", "--host", "0.0.0.0", "--port", "8000"]
