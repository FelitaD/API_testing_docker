#!/bin/bash

export DOCKER_BUILDKIT=0
export COMPOSE_DOCKER_CLI_BUILD=0

docker image build . -t test_authentification -f test_authentification.Dockerfile
docker image build . -t test_authorization -f test_authorization.Dockerfile
docker image build . -t test_content -f test_content.Dockerfile

docker-compose up
