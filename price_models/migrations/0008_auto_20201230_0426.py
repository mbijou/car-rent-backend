# Generated by Django 3.1.4 on 2020-12-30 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price_models', '0007_auto_20201230_0426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyprice',
            name='day',
            field=models.IntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')]),
        ),
    ]
