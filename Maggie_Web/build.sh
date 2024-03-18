#/bin/bsh

#build the project

echo "building the project..."
python3.9 -m pip install -r Future-Energy/blob/main/Maggie_Web/requirements.txt

echo "make migrations..."
python3.9 manage.py makemigrations 
python3.9 manage.py migrate

echo "collect static"
python3.9 manage.py collectstatic

