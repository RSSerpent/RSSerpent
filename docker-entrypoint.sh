#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset
# set -o xtrace

APP_PATH="/app"

if [[ "$1" == "poetry" ]]; then
  mkdir -p "$APP_PATH"
  chown -R RSSerpent:RSSerpent "$APP_PATH"
  echo "run server as user RSSerpent"
  gosu RSSerpent "$@"
else
  exec "$@"
fi
