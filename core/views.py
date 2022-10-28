from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>welcome to django social network</h1>')

