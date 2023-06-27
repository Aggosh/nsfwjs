# Django example

Layered with Django, Django records all uploaded pictures and response.


# Install

Create .env file in this folder with parameters


```
POSTGRES_DB = 'django_nsfwjs'
POSTGRES_USER = 'postgres'
POSTGRES_PASSWORD = 'Aggosh'
POSTGRES_HOST = 'localhost'
POSTGRES_PORT = 5432

DJANGO_DEBUG = True
DJANGO_ALLOWED_HOSTS = '*'
DJANGO_SECRET_KEY = 'XXX'

NODE_SERVER_URL = "http://127.0.0.1:8080"
```

Run docker-compose

```
docker-compose  up --build
```

Now Django run in port 8000

### This project can't work on Windows or macOS with M1 and M2
There is an issue where node tensorflow doesn't work in Docker on these systems.