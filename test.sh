#!/bin/sh

echo "Starting test preparation..."

# Wait for PostgreSQL to be available
echo "Waiting for PostgreSQL to start..."
while ! nc -z db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

# Run migrations to ensure the database schema is up to date
echo "Running migrations..."
python3 manage.py migrate --noinput

# Collect static files (if needed)
echo "Collecting static files..."
python3 manage.py collectstatic --noinput

# Run tests
echo "Running tests..."
python3 manage.py test --verbosity=2

echo "Test run completed."
