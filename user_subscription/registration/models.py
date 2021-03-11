from django.db import models
from django.contrib.auth.models import AbstractUser
from djstripe.models import Customer, Subscription

# Create your models here.


class CustomUser(AbstractUser):
    customer = models.ForeignKey(
        Customer, null=True, blank=True, on_delete=models.SET_NULL
    )
    subscription = models.ForeignKey(
        Subscription, null=True, blank=True, on_delete=models.SET_NULL
    )
    password = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    USERNAME_FIELD = "username"
