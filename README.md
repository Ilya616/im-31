# im-31

что делаем: https://htmldemo.net/cigar/cigar/index.html

python -m venv .venv
django-admin startproject mysite
python manage.py runserver
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.venv\Scripts\Activate.ps1

./manage.py makemigrations im
python manage.py makemigrations
python manage.py migrate
