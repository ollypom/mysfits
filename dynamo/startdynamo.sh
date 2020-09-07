#!/bin/bash

docker run \
    --detach \
    --name dynamodb-local \
    --publish 8000:8000 \
    amazon/dynamodb-local:latest \