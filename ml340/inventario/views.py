from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect

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
        return HttpResponseRedirect("/inventario/read")

        
          
    context['form']= form
    return render(request, 'inventario/create.html', context)
    #return HttpResponse("Inventario Create")

class read(generic.ListView,):
    model = Item
    template_name = 'inventario/read.html'

def detail_read(request, id):
    context = {}
    context["data"] = Item.objects.get(id=id)
    return render(request,'inventario/detail_read.html',context)
    

def update(request,id):
    context={}

    obj = get_object_or_404(Item, id=id)

    form = ItemsForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/inventario/read/"+id)

    context["form"]=form

    return render(request,'inventario/update.html',context)


    

def delete(request, id):
    context={}
    
    obj=get_object_or_404(Item, id = id)

    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/inventario/read")

    return render(request, 'inventario/delete.html', context)

