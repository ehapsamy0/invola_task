from enum import unique
from operator import mod
from django.db import models

# Create your models here.


class Shipment(models.Model):
    transfer_id = models.CharField(max_length=50,unique=True)    
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)


class ShipmentItem(models.Model):
    shipment = models.ForeignKey(Shipment,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)    
    width = models.FloatField()
    hight = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

