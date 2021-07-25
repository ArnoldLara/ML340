from django.shortcuts import render
from django.http import HttpResponse

from .models import Specification, Manufacturer, Category, Network, Status, Item
# Create your views here.
from django.views import generic
from .forms import ItemsForm


def index(request):
    #return HttpResponse("Hello World")
    items = Item.objects.all()
    pc = Item.objects.filter(category__name__icontains='PC').count()
    switch = Item.objects.filter(category__name__icontains='Switch').count()
    router = Item.objects.filter(category__name__icontains='Router').count()
    context = {'pc':pc, 'switch':switch, 'router':router}
    #return HttpResponse("Inventario Read")
    return render(request,"inventario/index.html",context)

def create(request):
     # dictionary for initial data with 
    # field names as keys
    context ={}
  
    # add the dictionary during initialization
    form = ItemsForm(request.POST or None)
    if form.is_valid():
        form.save()
          
    context['form']= form
    return render(request, 'inventario/create.html', context)
    #return HttpResponse("Inventario Create")

class read(generic.ListView):
    model = Item
    template_name = 'inventario/read.html'

def update(request):
    return HttpResponse("Inventario Update")

def delete(request):
    return HttpResponse("Inventario Delete")