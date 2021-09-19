#!/bin/sh

poetry export -o requirements.txt --without-hashes
docker build . -t rsserpent
