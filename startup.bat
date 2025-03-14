@echo off
cd django-blog
python3.13 manage.py runserver 0.0.0.0:8000 --insecure
cd ..
