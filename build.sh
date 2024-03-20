#/bin/bsh

#build the project
<<<<<<< HEAD
echo "building the project..."
python3.9 -m pip install -r requirements.txt

echo "make migrations..."
python3.9 manage.py makemigrations
python3.9 manage.py migrate

echo "collect static"
python3.9 manage.py collectstatic
=======

python3 -m pip install -r requirements.txt

python3 manage.py makemigrations
python3 manage.py migrate

python3 manage.py collectstatic



>>>>>>> 79f5c16878b23459501ba42651c472ebad70d3c7




