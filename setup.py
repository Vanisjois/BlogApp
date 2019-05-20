# Execute from terminal
# Install pip
python -m ensurepip

# Install django
python -m pip install django

# Find django version
python -m django --version

# Get list of commands in django
django-admin

# create new project in django
django-admin startproject django_project

# command to run the server, run from inside the django_project
python manage.py runserver

# command to create a new app
python manage.py startapp blog

