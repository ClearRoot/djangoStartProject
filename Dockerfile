FROM python:3.9.0

WORKDIR /home/

RUN git clone -b main --single-branch https://github.com/ClearRoot/djangoStartProject.git

WORKDIR /home/djangoStartProject/

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py makemigrations --settings=djangoStartProject.settings.deploy &&\
 python manage.py migrate --settings=djangoStartProject.settings.deploy &&\
 python manage.py collectstatic --noinput --settings=djangoStartProject.settings.deploy &&\
 gunicorn --env DJANGO_SETTINGS_MODULE=djangoStartProject.settings.deploy djangoStartProject.wsgi --bind 0.0.0.0:8000"]
