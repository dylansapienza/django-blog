from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("<html><head></head><body><h1>Hey there!</h1></body> </html>")
