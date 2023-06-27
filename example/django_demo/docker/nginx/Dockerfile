FROM nginx:1.23.4-alpine

WORKDIR /var/www/app

ADD example/django_demo/docker/nginx/app.conf /etc/nginx/conf.d/default.conf

COPY example/django_demo/staticfiles /var/www/app/staticfiles
