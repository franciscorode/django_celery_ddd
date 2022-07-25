#!/bin/bash
set -Eeo pipefail

celery -A src worker -l INFO