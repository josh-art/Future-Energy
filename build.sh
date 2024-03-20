<<<<<<< HEAD:build.sh
#/bin/bsh

#build the project

pip install -r requirements.txt

python3.9 manage.py collectstatic

python3.9 manage.py makemigrations
python3.9 manage.py migrate





=======
#/bin/bsh

#build the project

python3 -m pip install -r requirements.txt

python3 manage.py collectstatic

python3 manage.py makemigrations
python3 manage.py migrate





>>>>>>> 1980a40f8339e4703f152007a89213799f485f94:Maggie_Web/build.sh
