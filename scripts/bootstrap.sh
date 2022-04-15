#!/usr/bin/env bash

# Exit when any command fails
set -e

BASE_DIR="$(realpath $(dirname $0)/..)"

echo -e "\u001b[34m=> Setting up local poetry instance...\u001b[0m"
curl -sSL https://install.python-poetry.org | POETRY_HOME="$BASE_DIR/poetry" POETRY_VERSION=1.1.13 python3.10 - -y > /dev/null
export PATH="$BASE_DIR/poetry/bin:$PATH"

cd $BASE_DIR

echo -e "\u001b[34m=> Setting up virtualenv and installing dependencies...\u001b[0m"
poetry install > /dev/null
source "$BASE_DIR/.venv/bin/activate"

echo -e "\u001b[34m=> Running database migrations...\u001b[0m"
$BASE_DIR/manage.py migrate > /dev/null

echo -e "\u001b[34m=> Collecting static files...\u001b[0m"
$BASE_DIR/manage.py collectstatic --noinput > /dev/null

echo -e "\u001b[32mDone!\u001b[0m"
