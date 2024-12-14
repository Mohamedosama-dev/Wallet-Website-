#!/bin/sh

# Function to wait for PostgreSQL to be available
wait_for_postgres() {
    echo "Waiting for PostgreSQL to be available..."
    while ! nc -z db 5432; do
        sleep 1
    done
    echo "PostgreSQL is up and running!"
}

# Wait for PostgreSQL
wait_for_postgres

# Run database migrations
echo "Running migrations..."
python manage.py migrate

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

ADMIN_EMAIL="admin@example.com"
ADMIN_PASSWORD="adminpassword"

if ! python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); print(User.objects.filter(email='$ADMIN_EMAIL').exists())"; then
    echo "Creating admin user..."
    echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('$ADMIN_EMAIL', '$ADMIN_EMAIL', '$ADMIN_PASSWORD')" | python manage.py shell
    echo "Admin user created with email $ADMIN_EMAIL"
else
    echo "Admin user already exists."
fi

# Start the Django development server
echo "Starting the Django server..."
exec python manage.py runserver 0.0.0.0:8001
