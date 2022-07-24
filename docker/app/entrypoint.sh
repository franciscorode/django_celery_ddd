#!/bin/bash
set -Eeo pipefail

dockerize -wait tcp://${POSTGRES_HOST}:5432 -timeout 30s
