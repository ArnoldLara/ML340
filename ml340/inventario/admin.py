from django.contrib import admin

# Register your models here.


from .models import Specification, Manufacturer, Category, Status, Item

admin.site.register(Specification)
admin.site.register(Manufacturer)
admin.site.register(Category)
admin.site.register(Status)
admin.site.register(Item)