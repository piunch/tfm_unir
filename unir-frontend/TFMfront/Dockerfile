FROM node:8

EXPOSE 8080

RUN mkdir -p /usr/node
WORKDIR /usr/node
COPY . /usr/node

CMD cd /usr/node && npm start

# docker build -t frontend .
# docker run --env NODE_ENV=test --env TOKEN_KEY=tost4da --name frontend --net testnet --ip 172.18.0.4 -p8080:8080 -dt frontend
