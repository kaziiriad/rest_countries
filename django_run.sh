cd rest_countries/
python manage.py makemigrations
python manage.py migrate
python manage.py fetch_countries
python manage.py runserver 0.0.0.0:8000