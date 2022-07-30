FROM node:18-bullseye-slim

RUN mkdir /app && chown -R node:node /app

WORKDIR /app
COPY ../svelte/package*.json /app 

RUN npm cache clean --force
RUN npm install 

USER node
