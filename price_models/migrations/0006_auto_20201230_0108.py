# Generated by Django 3.1.4 on 2020-12-30 01:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('price_models', '0005_auto_20201230_0024'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PricePerDay',
            new_name='DailyPrice',
        ),
    ]
