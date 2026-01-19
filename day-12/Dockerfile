# Use small, production-friendly base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependencies first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy your FastAPI app
COPY day_12.py .

# Expose port
EXPOSE 8000

# Command to run app in container
CMD ["uvicorn", "day_12:app", "--host", "0.0.0.0", "--port", "8000"]
