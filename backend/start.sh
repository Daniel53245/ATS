#!/bin/bash

echo "⏳ Waiting for database to be ready..."
until python -c "import psycopg2; psycopg2.connect(host='db', port=5432, user='user', password='password', dbname='jobtracker')" >/dev/null 2>&1; do
  echo "🔄 Still waiting for db..."
  sleep 1
done

echo "✅ Database is ready!"

# Alembic
rm -rf alembic/versions/*
alembic revision --autogenerate -m "init"
alembic upgrade head

# Run FastAPI
exec uvicorn app.main:app --host 0.0.0.0 --port 8000 
