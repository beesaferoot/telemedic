FROM python:3.6.9
ADD . /app
WORKDIR /app
ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app \
    DATABASE_URL= 

EXPOSE 8000
COPY requirements.txt /app/
RUN pip install -r requirements.txt
RUN python manage.py makemigrations && python manage.py migrate
RUN ./load-tests.sh
# Run application
CMD python manage.py runserver 
