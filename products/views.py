from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index (request):
    return HttpResponse('Hello World') #arguments to the constructor

def new(request):
    return HttpResponse('new products')