.PHONY: all build-frontend push-frontend build-backend push-backend

NAME     = {{cookiecutter.project_slug}}
REGISTRY = docker-registry.dglecom.net
TAG      = $$(git log -1 --pretty=%h)
VERSION  = ${NAME}:${TAG}
LATEST   = ${REGISTRY}/${NAME}:latest

BUILD_REPO_ORIGIN	= $$(git config --get remote.origin.url)
BUILD_COMMIT_SHA1	= $$(git rev-parse --short HEAD)
BUILD_COMMIT_DATE	= $$(git log -1 --date=short --pretty=format:%ct)
BUILD_BRANCH		= $$(git symbolic-ref --short HEAD)
BUILD_DATE 			= $$(date -u +"%Y-%m-%dT%H:%M:%SZ")


all: build-frontend push-frontend build-backend push-backend


build-frontend:
	docker build --rm -t  -t ${REGISTRY}/${NAME}:latest -t ${REGISTRY}/${NAME}:${TAG} -t ${NAME}:${TAG} -t ${NAME}:latest  \
	--build-arg BUILD_COMMIT_SHA1=${BUILD_COMMIT_SHA1} \
	--build-arg BUILD_COMMIT_DATE=${BUILD_COMMIT_DATE} \
	--build-arg BUILD_BRANCH=${BUILD_BRANCH} \
	--build-arg BUILD_DATE=${BUILD_DATE} \
	--build-arg BUILD_REPO_ORIGIN=${BUILD_REPO_ORIGIN} \
	 -f docker/DockerfileFrontendDistribute .

build-backend:
	docker build --rm -t ${REGISTRY}/{{cookiecutter.project_slug}}-backend:latest  -t ${REGISTRY}/{{cookiecutter.project_slug}}-backend:${BUILD_COMMIT_SHA1} -t {{cookiecutter.project_slug}}:${BUILD_COMMIT_SHA1} -t {{cookiecutter.project_slug}}:latest  \
	--build-arg BUILD_COMMIT_SHA1=${BUILD_COMMIT_SHA1} \
	--build-arg BUILD_COMMIT_DATE=${BUILD_COMMIT_DATE} \
	--build-arg BUILD_BRANCH=${BUILD_BRANCH} \
	--build-arg BUILD_DATE=${BUILD_DATE} \
	--build-arg BUILD_REPO_ORIGIN=${BUILD_REPO_ORIGIN} \
	 -f docker/DockerfileBackend .

push-frontend:
	docker push ${REGISTRY}/${NAME}:latest
	docker push ${REGISTRY}/${NAME}:${TAG}

push-backend:
	docker push ${REGISTRY}/{{cookiecutter.project_slug}}-backend:latest
	docker push ${REGISTRY}/{{cookiecutter.project_slug}}-backend:${TAG}
