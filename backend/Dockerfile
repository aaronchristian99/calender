FROM python:3.8-slim

WORKDIR /app

COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN alembic upgrade head

COPY backend .

CMD ["python", "server.py"]