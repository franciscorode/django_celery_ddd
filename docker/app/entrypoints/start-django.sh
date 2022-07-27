#!/bin/bash
set -Eeo pipefail

python3.9 manage.py collectstatic --noinput -v 0
python3.9 manage.py migrate --noinput

# Start app
echo "Starting application"
if [ "${DEPLOY_ENVIRONMENT:-x}" = "LOCAL" ]; then
    python3.9 manage.py runserver 0.0.0.0:8000
else
    gunicorn src.config.asgi:application \
        -k uvicorn.workers.UvicornWorker \
        --bind :8000 \
        --log-level error \
        --timeout 30
        --reload
fi