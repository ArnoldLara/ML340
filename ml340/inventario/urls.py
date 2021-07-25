from django.urls import path

from . import views


app_name = 'inventario'
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('read', views.read.as_view(), name='read'),
    path('update', views.update, name='update'),
    path('delete', views.delete, name='delete'),

    
]