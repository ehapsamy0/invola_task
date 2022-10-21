from email.headerregistry import Address
from email.policy import default
from operator import mod
from statistics import mode
from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

class Courier(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    name = models.CharField(max_length=150,unique=True)
    address = models.CharField(max_length=250)
    phone = models.CharField(validators=[phone_regex], max_length=15,unique=True)    
    can_canceld = models.BooleanField(default=False)
    active  = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}"
