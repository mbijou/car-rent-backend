# Generated by Django 3.1.4 on 2021-01-02 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('manufacturers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('truck', 'truck'), ('car', 'car')], max_length=200)),
                ('model', models.CharField(max_length=200)),
                ('manufacturer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='manufacturers.manufacturer')),
            ],
        ),
    ]
