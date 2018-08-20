FROM cypress/base:10
RUN npm install --save-dev cypress
RUN $(npm bin)/cypress verify

WORKDIR /app

CMD $(npm bin)/cypress run
