from django.shortcuts import render
from django.http import HttpResponse

from .models import Specification, Manufacturer, Category, Network, Status, Item
# Create your views here.

def index(request):
    #return HttpResponse("Hello World")
    return render(request,"inventario/index.html")

def create(request):
    
    return HttpResponse("Inventario Create")

def read(request):
    items = Item.objects.all()
    num_items = Item.objects.all().count()
    context = {'items':items, 'num_items':num_items}
    #return HttpResponse("Inventario Read")
    return render(request,"inventario/read.html",context)

def update(request):
    return HttpResponse("Inventario Update")

def delete(request):
    return HttpResponse("Inventario Delete")