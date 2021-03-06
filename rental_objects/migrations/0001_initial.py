# Generated by Django 3.1.4 on 2021-01-02 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('properties', '0001_initial'),
        ('price_models', '0001_initial'),
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RentalObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_of_manufacture', models.IntegerField()),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cars.car')),
                ('price_models', models.ManyToManyField(blank=True, to='price_models.PriceModel')),
                ('properties', models.ManyToManyField(blank=True, to='properties.PropertyValue')),
            ],
        ),
    ]
