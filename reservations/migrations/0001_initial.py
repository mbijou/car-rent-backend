# Generated by Django 3.1.4 on 2020-12-29 23:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('price_models', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rental_objects', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pick_up_datetime', models.DateTimeField()),
                ('return_datetime', models.DateTimeField()),
                ('not_registered_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.notregistereduser')),
                ('rental_object', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='rental_objects.rentalobject')),
                ('rental_object_price_model', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='price_models.rentalobjectpricemodel')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
