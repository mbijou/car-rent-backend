# Generated by Django 3.1.4 on 2020-12-26 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0003_auto_20201226_1802'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=200)),
                ('house_number', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('postal_code', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='notregistereduser',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reservations.address'),
        ),
    ]
