{{cookiecutter.project_name}}
=============================

Do stuff with react frontend and a backend


## Installation

Docker compose is used and bundles all the toys

**DO NOT** just docker-compose up.
You must follow the steps below for maxiumum happiness.

```
docker-compose up db                                       # let the db get created first (no dont use that docker-wait thing its crap)
#
# following are required because we mount the host filesystem SRC into the container, so you need to install node_modules on local fs.
# and with django you gotta create the db
#
docker-compose run --rm frontend yarn install              # install modules to host fs 
docker-compose run --rm backend python manage.py migrate   # create db
docker-compose run --rm mock-backend yarn install          # install modules to host fs 
```

Development
-----------

**start services in groups so you dont have to restart all of them**

1. docker-compose up db
2. docker-compose up nginx mailcatcher
3. docker-compose up frontend
4. docker-compose exec frontend npm test
5. docker-compose up backend
6. docker-compose up mock-backend

Compose mounts your local source in the running container so you can just edit it with your IDE as you would normally

Each time you add a new requirement to requirements.txt you will need to docker-compose up --build backend (so it installs to the container)

Via Nginx
---------

http://localhost/
http://localhost/mock-api/products
http://localhost/api/products

Direct
------

http://localhost:3000
http://localhost:8001/products
http://localhost:8000/products


DB migrations
-------------

**django manage.py**

runs db migration and custom commands

```
docker-compose run --rm -w /src/ backend python manage.py

docker-compose run --rm -w /src/ backend python manage.py makemigrations
docker-compose run --rm -w /src/ backend python manage.py migrate
docker-compose run --rm -w /src/ backend python manage.py shell_plus
```

**Postgres**

Postgres starts up on the exposed 5432 port by default, you can interact with it as you would normally.


**Shell access**

```
docker-compose run --rm frontend sh
docker-compose run --rm backend sh
```

**Running commands on running container**

Yes you can also use `run` instead of `exec`. Exec just expects the container to be running already.

```
docker-compose exec frontend sh
docker-compose exec backend python manage.py shell_plus
```

Building and Publishing (usually out of dev hands)
--------------------------------------------------


**Build and tag image for local**

Tags the image locally

1. {{cookiecutter.project_slug}}:latest  # local latest
2. on the build server, the following commands can be called. This puts control of the build process (and testing) fully in your hands.

```
make build-frontend
make build-backend
make build-mockbackend

# push (usually done by CI server)

make push-frontend
make push-backend
```


**Do check if application is live by using the following endpoint**

Developers should provide a route for this path segement

```
 /health
```

# Backend

developed with base of: https://github.com/cescgie/lumen-rest-api


# secret

webdev
l1pst1cks



# helper 

php artisan wn:resource producttest "id;numeric;required;fillable name;string;required;fillable title;string;required;fillable description;string;required;fillable from;datetime;required;fillable to;numeric;required;fillable image;string;required;fillable status;string;required;fillable"

## ERRORS

```
docker-compose run --rm -w /src/ -u www-data backend composer dump-autoload
```

## FRONTEND THEME WITH SEMANTIC

read:

1. https://github.com/typicode/json-server
2. https://github.com/dfsq/json-server-init
3. https://github.com/json-schema-faker/json-schema-faker#swagger-extensions

handled in docker files

https://github.com/marak/Faker.js/

```
npm install -g create-react-app
npm install -g json-server-init
npm install -g json-server
```


## WINDOWS 10 PROBLEM(s)
Windows has an unique HTTP service that manages calls to IIS and other HTTP enabled services, such as "Microsoft-HttpApi/2.0".
To stop this, follow these step:
* Uninstall the IIS by Turn on/off windows features
* Type-in with PS `net stop http`



