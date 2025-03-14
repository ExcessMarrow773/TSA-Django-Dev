@echo off
cd django-blog
python3.13 manage.py makemigrations
if %ERRORLEVEL% neq 0 exit /b %ERRORLEVEL%
python3.13 manage.py migrate
cd ..
