release: python manage.py migrate && ./load-tests.sh
web: gunicorn main.wsgi --log-file -