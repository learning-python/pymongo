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