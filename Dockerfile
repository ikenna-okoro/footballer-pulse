# Base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy application code
COPY . /app

# Update system packages and install dependencies
RUN apt-get update && apt-get upgrade -y && apt-get clean && \
	pip install --no-cache-dir -r requirements.txt

# Expose the port Flask runs on
EXPOSE 5000

# Command to run the application
CMD ["python3", "main.py"]