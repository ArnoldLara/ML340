from enum import unique
from django.db import models

# Create your models here.



class Specification(models.Model):
    model = models.CharField(max_length=50)
    processor = models.CharField(max_length=50)
    ram = models.CharField(max_length=50, help_text="Ingrese la cantidad junto a la unidad MB o GB(4 GB)")
    dd = models.CharField(max_length=50, help_text="Ingrese la cantidad junto a la unidad MB o GB(500 GB)")

    def __str__(self):
        return self.model

class Manufacturer(models.Model):
    
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Category(models.Model):
    
    name = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField(default=0)
    #Historico de cantidad para asignar nombres
    h_quantity = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.name


class Status(models.Model):
    item = models.OneToOneField('Item',on_delete=models.CASCADE, null=True)
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='a', help_text='Disponibilidad del Recurso')
    def __str__(self):
        return self.status

class Item(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    serial_number = models.CharField(unique=True, max_length=50)
    serial_andes = models.DecimalField(blank=True, unique=True, max_digits=50, decimal_places=0)
    specs = models.ForeignKey(Specification,on_delete=models.SET_NULL, null=True, blank=True)
    mac = models.CharField(max_length=17, blank=True, help_text="4a:c6:b2:40:89:f9")
    ip = models.CharField(max_length=15, blank=True, help_text="172.21.99.54")
    reserva_ip = models.BooleanField(default=False)
    notes = models.CharField(max_length=1000, blank=True)
    def __str__(self):
        return self.name