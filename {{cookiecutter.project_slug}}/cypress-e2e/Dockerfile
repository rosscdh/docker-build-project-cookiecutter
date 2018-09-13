FROM cypress/base:10

WORKDIR /app

COPY ./cypress-e2e/package.json /app
COPY ./cypress-e2e/cypress.json /app
COPY ./cypress-e2e/cypress /app/cypress

RUN npm install
RUN $(npm bin)/cypress verify

CMD $(npm bin)/cypress run
