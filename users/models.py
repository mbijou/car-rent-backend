from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.


class Profile(models.Model):
    address = models.ForeignKey("users.Address", null=True, on_delete=models.SET_NULL)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Address(models.Model):
    street = models.CharField(max_length=200)
    house_number = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=200)


class NotRegisteredUser(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    profile = models.ForeignKey('users.NotRegisteredProfile', on_delete=models.CASCADE)


class NotRegisteredProfile(models.Model):
    address = models.ForeignKey("users.Address", null=True, on_delete=models.SET_NULL)
