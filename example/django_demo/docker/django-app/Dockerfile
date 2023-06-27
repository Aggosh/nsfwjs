FROM python:3.11

WORKDIR /app

ADD ../../django_nsfwjs django_nsfwjs/
ADD ../../user_interface user_interface/
ADD ../../manage.py .
ADD ../../requirements.txt .
RUN mkdir media/

RUN pip3 install -r requirements.txt

EXPOSE 8000
