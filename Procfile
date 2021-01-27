release: python manage.py migrate
release: ./load-tests.sh
web: gunicorn main.wsgi --log-file -