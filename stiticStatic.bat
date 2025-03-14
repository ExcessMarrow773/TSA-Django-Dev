@echo off
cd django-blog
python3.13 manage.py collectstatic
echo You should be good to go!
cd ..
 