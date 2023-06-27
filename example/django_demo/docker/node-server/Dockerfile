FROM ubuntu:latest
USER root
WORKDIR /app/example/node/server

COPY example/django_demo/node-server .
COPY package.json .
RUN apt-get update
RUN apt-get -y install curl gnupg
RUN curl -sL https://deb.nodesource.com/setup_16.x  | bash -
RUN apt-get -y install nodejs
RUN npm i express multer jpeg-js @tensorflow/tfjs-node
RUN npm install

EXPOSE 8080