The Dashboard webpage is based on Python Flask.

1. How to start the server:

>> python manage.py runserver

if you want to change host port or anything else:

>> python manage.py runserver --help



2. Environment

All the requirements are listed in requirements.txt. 

You can use the virtualenv by:
>> pip install virtualenv
>> source ./virtualenv/bin/activate
>> deactivate



3. App

The main back-end code is in app/main/views.py

The static files are in app/static/newdash

The front-end code is in templates/newdash/index.html

The js code which deals with the data from back-end is in app/static/phil/draw-charts.js



4. More Information

contact phillu@126.com