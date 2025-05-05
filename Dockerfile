# Use official Python slim image
FROM python:3.10-bookworm

# Set working directory
WORKDIR /app

# Copy app files
COPY app/ .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Start API server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
