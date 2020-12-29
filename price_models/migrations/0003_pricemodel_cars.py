# Generated by Django 3.1.4 on 2020-12-27 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_car_price_models'),
        ('price_models', '0002_carpricemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricemodel',
            name='cars',
            field=models.ManyToManyField(through='price_models.CarPriceModel', to='cars.Car'),
        ),
    ]