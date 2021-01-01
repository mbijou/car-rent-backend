# Generated by Django 3.1.4 on 2020-12-30 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('price_models', '0008_auto_20201230_0426'),
        ('reservations', '0002_remove_reservation_rental_object_price_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='price_model',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='price_models.pricemodel'),
        ),
    ]