#!/bin/sh
echo "Waiting for PostgreSQL to start..."

# Wait for PostgreSQL to be available
while ! nc -z db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

# Run Django tests
python3 manage.py test --verbosity=2
