from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello World")

def create(request):
    return HttpResponse("Inventario Create")

def read(request):
    return HttpResponse("Inventario Read")

def update(request):
    return HttpResponse("Inventario Update")

def delete(request):
    return HttpResponse("Inventario Delete")