#!/usr/bin/env bash

# Exit when any command fails
set -e

export BASE_DIR="$(realpath $(dirname $0)/..)"

envsubst < "$BASE_DIR/apache/cclc_queue.conf" > /etc/httpd/conf.d/cclc_queue.conf
