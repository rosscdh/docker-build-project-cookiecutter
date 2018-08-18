.PHONY: all build-frontend build-mockbackend build-backend push-frontend push-backend push-mockbackend

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

push-frontend:
	docker push ${REGISTRY}/${LATEST}
	docker push ${REGISTRY}/${VERSION}

push-backend:
	docker push ${REGISTRY}/{{cookiecutter.project_slug}}-backend:latest
	docker push ${REGISTRY}/{{cookiecutter.project_slug}}-backend:${TAG}

push-mockbackend:
	docker push ${REGISTRY}/{{cookiecutter.project_slug}}-mockbackend:latest
	docker push ${REGISTRY}/{{cookiecutter.project_slug}}-mockbackend:${TAG}
