FROM cypress/base:10

WORKDIR /app

ADD ./cypress-e2e /app

RUN npm install
RUN $(npm bin)/cypress verify

CMD ["$(npm bin)/cypress", "run"]
