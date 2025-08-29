docker-compose build
docker-compose up -d



docker-compose exec web python3 manage.py migrate
docker-compose exec web python3 manage.py createsuperuser


docker-compose down
docker-compose build --no-cache
