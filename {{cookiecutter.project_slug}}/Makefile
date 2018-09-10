.PHONY: all build-frontend build-mockbackend build-backend push-frontend push-backend push-mockbackend build-e2e e2e

NAME     = {{cookiecutter.project_slug}}
REGISTRY = {{cookiecutter.docker_registry}}
TAG      = $$(git log -1 --pretty=%h)
VERSION  = ${NAME}:${TAG}
LATEST   = ${NAME}:latest

BUILD_REPO_ORIGIN	= $$(git config --get remote.origin.url)
BUILD_COMMIT_SHA1	= $$(git rev-parse --short HEAD)
BUILD_COMMIT_DATE	= $$(git log -1 --date=short --pretty=format:%ct)
BUILD_BRANCH		= $$(git symbolic-ref --short HEAD)
BUILD_DATE 			= $$(date -u +"%Y-%m-%dT%H:%M:%SZ")


all: build-frontend build-mockbackend build-backend push-frontend push-backend push-mockbackend


build-frontend:
	docker build --rm -t ${REGISTRY}/${LATEST} -t ${REGISTRY}/${VERSION} -t ${VERSION} -t ${LATEST}  \
	--build-arg BUILD_COMMIT_SHA1=${BUILD_COMMIT_SHA1} \
	--build-arg BUILD_COMMIT_DATE=${BUILD_COMMIT_DATE} \
	--build-arg BUILD_BRANCH=${BUILD_BRANCH} \
	--build-arg BUILD_DATE=${BUILD_DATE} \
	--build-arg BUILD_REPO_ORIGIN=${BUILD_REPO_ORIGIN} \
	 -f docker/DockerfileFrontendDistribute .

build-mockbackend:
	docker build --rm -t ${REGISTRY}/{{cookiecutter.project_slug}}-mockbackend:latest -t ${REGISTRY}/{{cookiecutter.project_slug}}-mockbackend:${BUILD_COMMIT_SHA1} -t {{cookiecutter.project_slug}}-mockbackend:${BUILD_COMMIT_SHA1} -t {{cookiecutter.project_slug}}-mockbackend:latest  \
	--build-arg BUILD_COMMIT_SHA1=${BUILD_COMMIT_SHA1} \
	--build-arg BUILD_COMMIT_DATE=${BUILD_COMMIT_DATE} \
	--build-arg BUILD_BRANCH=${BUILD_BRANCH} \
	--build-arg BUILD_DATE=${BUILD_DATE} \
	--build-arg BUILD_REPO_ORIGIN=${BUILD_REPO_ORIGIN} \
	 -f docker/DockerfileBackend .

build-backend:
	docker build --rm -t ${REGISTRY}/{{cookiecutter.project_slug}}-backend:latest -t ${REGISTRY}/{{cookiecutter.project_slug}}-backend:${BUILD_COMMIT_SHA1} -t {{cookiecutter.project_slug}}-backend:${BUILD_COMMIT_SHA1} -t {{cookiecutter.project_slug}}-backend:latest  \
	--build-arg BUILD_COMMIT_SHA1=${BUILD_COMMIT_SHA1} \
	--build-arg BUILD_COMMIT_DATE=${BUILD_COMMIT_DATE} \
	--build-arg BUILD_BRANCH=${BUILD_BRANCH} \
	--build-arg BUILD_DATE=${BUILD_DATE} \
	--build-arg BUILD_REPO_ORIGIN=${BUILD_REPO_ORIGIN} \
	 -f docker/DockerfileBackend .

build-cypress:
	docker build -t cypress-e2e:latest -f cypress-e2e/Dockerfile .

run-cypress:
	docker run --rm -it -v ${PWD}/cypress-e2e:/app cypress-e2e:latest bash

push-frontend:
	docker push ${REGISTRY}/${LATEST}
	docker push ${REGISTRY}/${VERSION}

push-backend:
	docker push ${REGISTRY}/{{cookiecutter.project_slug}}-backend:latest
	docker push ${REGISTRY}/{{cookiecutter.project_slug}}-backend:${TAG}

push-mockbackend:
	docker push ${REGISTRY}/{{cookiecutter.project_slug}}-mockbackend:latest
	docker push ${REGISTRY}/{{cookiecutter.project_slug}}-mockbackend:${TAG}

start-mock-backend:
	docker stop mock-backend | true
	docker run -d --rm --name mock-backend -v ${PWD}/mock-backend:/src -p 8001:8001 tester_mock-backend:latest

start-frontend:
	docker stop frontend | true
	docker run -d --rm --name frontend -v ${PWD}/frontend:/src -p 3000:3000 --link mock-backend tester_frontend:latest

e2e: start-mock-backend start-frontend
	sleep 5
	docker run --rm -it -v ${PWD}/frontend:/app --link frontend:frontend cypress-e2e:latest
	docker stop frontend | true
	docker stop mock-backend | true