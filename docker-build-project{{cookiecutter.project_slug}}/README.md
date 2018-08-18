{{cookiecutter.project_name}}
========================

Do stuff with react frontend and a php backend


## Installation

Docker compose is used and bundles all the toys

```
npm install -g create-react-app
npm install -g json-server-init
npm install -g json-server
```

```
docker-compose up db                                       # let the db get created
docker-compose up                                          # will install the apps as well as nginx, percona, but wont finish frontend because it needs the `node_modules` installed
docker-compose run --rm frontend yarn install              # install/update the npm libs but use yarn because yarn is "better"
docker-compose run --rm -w /src/ backend composer install  # install/update the php libs
```

Development
-----------

**Edit your hosts**

1. Add the 2 urls that seperates admin from public view.
2. we use a plit horizon DNS which will expose the .pub.svc (public) address to the world
3. but only expose the .svc address to people inside douglas network

vim /etc/hosts

```
127.0.0.1   produkt-tester.pub.svc.dglecom.net        # PUBLIC /api
127.0.0.1   produkt-tester-admin.svc.dglecom.net      # ADMIN / and /api (which rewrites to /admin/api)
```

**public**
produkt-tester.pub.svc.dglecom.net/api    <-- post,get etc

**admin**
produkt-tester-admin.svc.dglecom.net/           <-- react admin frontend
produkt-tester-admin.svc.dglecom.net/api        <-- admin backend, which rewrites to /admin/api route


## DB migrations

https://laravel.com/docs/5.6/migrations

```
docker-compose run --rm -w /src/ backend php artisan migrate  # install the php libs
docker-compose run --rm -w /src/ backend php artisan db:seed  # seed with fake data - https://laravel.com/docs/5.6/seeding
```

## Once the images are built and running

`http://produkt-tester.pub.svc.dglecom.net`       - will hit your react app via nginx
`http://produkt-tester.pub.svc.dglecom.net/api`   - will hit the PUBLIC php backend via nginx
`http://produkt-tester-admin.svc.dglecom.net/api`       - will hit the ADMIN php backend via nginx


**artisan**

runs db migration and custom commands

```
docker-compose run --rm -w /src/ backend php artisan                # lists commands

docker-compose run --rm -w /src/ backend php artisan migrate        # migrates the database
docker-compose run --rm -w /src/ backend php artisan db:seed        # puts random stuff in the tables
docker-compose run --rm -w /src/ backend php artisan migrate:status # shows you table migration status
```

**Mysql**

Percona mysql starts up on the exposed 3306 port by default, you can interact with it as you would normally.


**Shell access**

```
docker-compose run --rm frontend sh
docker-compose run --rm backend sh
```

**Running commands on running container**

Yes you can also use `run` instead of `exec`. Exec just expects the container to be running already.

```
docker-compose exec frontend sh
docker-compose exec backend php artisan make:migration create_users_table --create=users
```

Building and Publishing (usually out of dev hands)
--------------------------------------------------


**Build and tag image for local**

Tags the image locally

1. {{cookiecutter.project_slug}}:latest  # local latest
2. on the build server, the following commands can be called. This puts control of the build process (and testing) fully in your hands.

```
make build-frontend   # you should turn this into a multi-stage dockerfile and run your tests before packaging the image
make build-backend   # you should turn this into a multi-stage dockerfile and run your tests before packaging the image

# push

make push-frontend
make push-backend
```


**Tag the image for remote**

When you run --rm this commmand it will set the tags for this build

1. docker-registry.dglecom.net/react-product-test:latest  # latest
2. docker-registry.dglecom.net/react-product-test:1v23gr  # git rev hash short, this hash is required to be specified for production deploys (we do not deploy latest)
3. react-product-test:latest  # local latest

```
make build-frontend tag
make build-backend tag
```


**Push the current image**
Push to the registry

```
make push
make set-backend push
```


**Do all of the above in one**

```
make all
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

We use semantic ui as a frontend design framework.
See https://semantic-ui.com and https://react.semantic-ui.com/introduction for introduction.
To change colors or settings of the theme, follow these steps:
* go to /semantic and run `npm install` and `npm install -g gulp`
* edit /semantic/semantic/src/themes/douglas/site.variables
* run `gulp build` in /semantic/semantic
* the file semantic.min.css in /frontend/src/css/semantic will be updated by this build process
* restart the react frontend and you will see the changes


## WINDOWS 10 PROBLEM(s)
Windows has an unique HTTP service that manages calls to IIS and other HTTP enabled services, such as "Microsoft-HttpApi/2.0".
To stop this, follow these step:
* Uninstall the IIS by Turn on/off windows features
* Type-in with PS `net stop http`



