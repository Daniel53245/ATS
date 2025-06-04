#!/bin/bash

echo "⏳ Waiting for database to be ready..."
until python -c "import psycopg2; psycopg2.connect(host='db', port=5432, user='user', password='password', dbname='jobtracker')" >/dev/null 2>&1; do
  echo "🔄 Still waiting for db..."
  sleep 1
done

echo "✅ Database is ready!"

# Optional: Clean up old migrations (if resetting)
rm -rf alembic/versions/*
echo "🧹 Cleaned old Alembic versions"

# Generate fresh migration
echo "📦 Generating migration..."
alembic revision --autogenerate -m "init"

# Apply it
echo "🚀 Applying migration..."
alembic upgrade head

# Start the server
echo "🌐 Starting FastAPI app..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
