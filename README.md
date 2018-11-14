# pymongo
PyMongo

In the terminal:
- [] Type `pip3 install pymongo` or `py -m pip3 install pymongo`
- [] Type `django-admin startproject pymongo_server`
- [] Type `cd pymongo_server`
- [] Type `python3 manage.py startapp mongo` or `py manage.py startapp drinks`
- [] In the pymongo_server/drinks/views.py file, enter this text:
```
from django.shortcuts import render
from django.http import HttpResponse
from . import mongo_controller
from json import loads

def index(request):
    return HttpResponse("Let's drink")

def whiskeys(request):
    if request.method == 'GET':
        res = mongo_controller.find('whiskeys')
        return HttpResponse(res)
    if request.method == 'POST':
        doc = loads(request.body)
        res = mongo_controller.insert_one('whiskeys', doc)
        return HttpResponse(res.inserted_id)
```
- [] Make a pymongo_server/drinks/urls.py file, and then enter this text:
```
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('whiskeys/', views.whiskeys, name='whiskeys'),
]
```
- [] In the pymongo_server/pymongo_server/urls.py file, replace the existing text with this text:
```
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('drinks/', include('drinks.urls')),
    path('admin/', admin.site.urls),
]
```
- [] Make a pymongo_server/drinks/mongo_controller.py file, and then enter this text:
```
import pymongo

client = pymongo.MongoClient('localhost', 27017)
drinks_db = client.drinks

def find(collection_name):
    collection = drinks_db[collection_name]
    return collection.find()

def insert_one(collection_name, doc):
    collection = drinks_db[collection_name]
    res = collection.insert_one(doc)
    return res
```
- [] Go to the pymongo_server/pymongo_server/settings.py file, find the `MIDDLEWARE` array, and comment out this line:
`'django.middleware.csrf.CsrfViewMiddleware',`
- [] Make sure you are still in the upper `pymongo_server` folder
- [] Type `python3 manage.py migrate` or `py manage.py migrate`
- [] Type `python3 manage.py runserver` or `py manage.py runserver`

Leave this terminal running and open up a second terminal. In this terminal:
- [] Type `mongod`

