from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return HttpResponse("This is the Homepage")

def school(response):
    return HttpResponse("<h1> Lucy is a teacher!!</h1>")