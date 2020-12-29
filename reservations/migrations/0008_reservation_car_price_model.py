# Generated by Django 3.1.4 on 2020-12-27 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('price_models', '0003_pricemodel_cars'),
        ('reservations', '0007_reservation_not_registered_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='car_price_model',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='price_models.carpricemodel'),
        ),
    ]