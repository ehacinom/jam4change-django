# https://tutorial.djangogirls.org

# start project
django-admin startproject myproject
cd myproject
python manage.py runserver

# settings
mate myproject/settings.py
# add 'app name' to INSTALLED_APPS
# TIME_ZONE = 'America/Chicago' # default as well :p
# path for static files
# STATIC_URL = '/assets/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# DEBUG = TRUE

# database
# database = model = obj
# https://www.tutorialspoint.com/django/django_creating_project.htm
python manage.py migrate

# app
python manage.py startapp myapp

# admin 
# was more complicated before : # https://www.tutorialspoint.com/django/django_admin_interface.htm
python manage.py createsuperuser # sei
python manage.py runserver

# A view function, or “view” for short, is simply a Python function that takes a web request and returns a web response. This response can be the HTML contents of a Web page, or a redirect, or a 404 error, or an XML document, or an image, etc. Example: You use view to create web pages, note that you need to associate a view to a URL to see it as a web page.

# go to myapp and make some views
# go to myapp/templates/ to make some templates
# go to myproject and make #include another urls pattern in urls.py
# go to myapp and make a file urls.py, the app's individual urlconfs

# Filters

* {{string|truncatewords:80}} − This filter will truncate the string, so you will see only the first 80 words.
* {{string|lower}} − Converts the string to lowercase.
* {{string|escape|linebreaks}} − Escapes string contents, then converts line breaks to tags.

# A model is a class that represents table or collection in our DB, and where every attribute of the class is a field of the table or collection. Models are defined in the app/models.py (in our example: myapp/models.py). Every model inherits from django.db.models.Model.

# Make your model

# make migrations
python manage.py makemigrations --empty myapp --name load_intial_data
# get sqlparse
# bulk insert from csv
python manage.py migrate


be careful about 
#!/usr/bin/env python
for wusgi in script and manage.py

# html - templates
cd app
mkdir templates
cd templates
mkdir app
cd app
mate post_list.html # save stuff


