cd /mnt/c/Users/ADMIN/Desktop/q\ -\ copy-gold/myproject
docker-compose down
docker-compose up -d
# Optionally, you might want to run migrations and collect static files
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py collectstatic --noinput
echo "Deployment completed."
