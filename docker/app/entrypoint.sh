#!/bin/bash
set -Eeo pipefail

dockerize -wait tcp://${POSTGRES_HOST}:5432 -timeout 30s

python3.9 manage.py collectstatic --noinput -v 0
python3.9 manage.py migrate --noinput

# Start app
echo "Starting application"
gunicorn src.config.asgi:application \
    -k uvicorn.workers.UvicornWorker \
    --bind :8000 \
    --log-level error \
    --timeout 30
