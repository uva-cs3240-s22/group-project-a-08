# Update BASEDIR
export DATABASE_URL=/OneDrive/Documents/GitHub/group-project-a-08/db.sqlite3

python manage.py makemigrations
python manage.py migrate

python manage.py runserver