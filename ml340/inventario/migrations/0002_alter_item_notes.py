# Generated by Django 3.2.5 on 2021-07-23 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='notes',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
