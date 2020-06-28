
# build stage
FROM node:lts-alpine 

WORKDIR /app
COPY package*.json ./

RUN npm install
RUN npm install -g @vue/cli
RUN npm i @vue/cli-service

COPY . .

CMD ["npm", "run", "serve"]