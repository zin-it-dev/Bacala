#!/bin/bash

# Wait for the database service to be ready
echo "Waiting for database..."
until nc -z $MYSQL_HOST $MYSQL_PORT; do
    sleep 1
done
echo "MySQL started"

# Run Flask-Migrate migrations
echo "Applying database migrations..."
flask db init
flask db migrate -m "Initial migration."
flask db upgrade

# Execute the command passed to the entrypoint (e.g., gunicorn)
exec "$@"