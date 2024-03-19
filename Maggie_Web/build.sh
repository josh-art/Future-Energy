#/bin/bsh

#build the project
echo "building the project..."
python3.9 -m pip install -r asgiref==3.7.2
Django==4.2.11
django-crispy-forms==2.1
pillow==10.2.0
psycopg2-binary==2.9.9
sqlparse==0.4.4
typing_extensions==4.10.0
tzdata==2024.1


echo "make migrations..."
python3.9 manage.py makemigrations 
python3.9 manage.py migrate

echo "collect static"
python3.9 manage.py collectstatic



