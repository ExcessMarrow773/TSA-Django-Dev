@echo off
python3 -m pip install -r requirements.txt
cd django-blog
python3 manage.py collectstatic
python3 manage.py runserver 0.0.0.0:8000
