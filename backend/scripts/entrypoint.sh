#!/bin/bash

# Ensure script fails on error
set -e

pip list

# Install requirements (ensure this runs in the correct directory)
pip install --no-cache-dir -r requirements.txt

echo "PORT is set to $PORT"

exec gunicorn --bind "0.0.0.0:$PORT" --workers 2 --threads 8 api.wsgi:application --preload --env DJANGO_SETTINGS_MODULE=api.settings
