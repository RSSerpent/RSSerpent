#!/bin/sh
set -e

if [ -f /app/runtime/requirements.txt ]; then
    pip install -r /app/runtime/requirements.txt
fi

exec "$@"
