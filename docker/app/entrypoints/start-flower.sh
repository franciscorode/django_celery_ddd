#!/bin/bash
set -Eeo pipefail

celery -A src --broker="${CELERY_BROKER}" flower