#!/bin/bash
set -e

# Build the Docker image
docker build -t agent-test .

# Run the container with mounted problems folder and .env
docker run --rm \
  --env-file .env \
  -v $(pwd)/problems:/app/problems \
  agent-test "$@"
