# Generated by Django 3.1.4 on 2020-12-29 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_property_multiple_choice'),
        ('rental_objects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentalobject',
            name='properties',
            field=models.ManyToManyField(blank=True, to='properties.PropertyValue'),
        ),
    ]
