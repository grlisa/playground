#!/bin/bash
set -e

# load from .env, if exists
if [ -f .env ]
then
  ENVVARS=$(cat .env | sed 's/#.*//g' | sed '/^$/d' | xargs -0)
  set -o allexport
  source .env
  set +o allexport
fi

NUM_WORKERS=${NUM_WORKERS:-2}
PORT=${APP_PORT:-8000}
TIMEOUT=${APP_TIMEOUT:-120}

echo "${tms} | Running DB initial fill ..."
poetry run python codebase/api/functions.py

poetry run gunicorn \
    codebase.main:app \
    -k uvicorn.workers.UvicornWorker \
    --workers $NUM_WORKERS \
    --bind 0.0.0.0:$PORT \
    --timeout $TIMEOUT \
    --preload
