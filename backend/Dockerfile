FROM python:3.8-slim

WORKDIR /app

# Install dependencies
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend directory
COPY backend .

CMD ["python", "server.py"]