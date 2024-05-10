# Utilisation d'une image de base avec Node.js et Python
FROM node:lts as builder

RUN apt-get update \
    && apt-get install -y python3 \
    python3-pip \
    python3-flask

WORKDIR /app

COPY package.json package-lock.json ./

RUN npm install

COPY . /app

ENV FLASK_DEBUG="true"
ENV FLASK_ENV="development"
