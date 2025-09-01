# Stage 1: Build Stage
FROM python:3.9-alpine AS builder

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Production Stage
FROM python:3.9-alpine

WORKDIR /app

# Copy only the installed packages from the builder stage
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages

# Copy the application code
COPY . .

# Create data directory
RUN mkdir -p data

# Command to run the application
CMD ["python", "run_app.py"]