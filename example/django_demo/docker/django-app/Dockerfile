FROM python:3.11

WORKDIR /app

ADD example/django_demo/django_nsfwjs django_nsfwjs/
ADD example/django_demo/user_interface user_interface/
ADD example/django_demo/manage.py .
ADD example/django_demo/requirements.txt .
RUN mkdir media/

RUN pip3 install -r requirements.txt

EXPOSE 8000
