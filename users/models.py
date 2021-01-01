from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from django.db.models.signals import post_save
from django.dispatch import receiver
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


class NotRegisteredProfile(models.Model):
    address = models.ForeignKey("users.Address", null=True, on_delete=models.SET_NULL)
    user = models.OneToOneField(NotRegisteredUser, null=True, on_delete=models.CASCADE, related_name="profile")


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(post_save, sender=NotRegisteredUser)
def create_not_registered_user_profile(sender, instance, created, **kwargs):
    if created:
        NotRegisteredProfile.objects.create(user=instance)


@receiver(post_save, sender=NotRegisteredUser)
def save_not_registered_user_profile(sender, instance, **kwargs):
    instance.profile.save()
