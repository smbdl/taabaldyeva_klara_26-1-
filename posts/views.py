from django.shortcuts import HttpResponse, redirect
from datetime import datetime

# Create your views here.


def hello_view(request):
    if request.method == 'GET':
        return HttpResponse("Hello! It's my project.")


def nowdate_view(request):
    if request.method == 'GET':
        return HttpResponse(datetime.now())


def goodbye_view(request):
    if request.method == 'GET':
        return HttpResponse("Goodbye user!")