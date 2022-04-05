#!/bin/sh/

# Add a database to use
export DATABASE_URL=./db.sqlite3

python manage.py makemigrations
python manage.py migrate

python manage.py runserver
