from enum import unique
from operator import mod
from django.db import models
from django.db.models.signals import post_migrate
from courier.models import Courier

# Create your models here.
class ShipmentStatus(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class Shipment(models.Model):
    transfer_id = models.CharField(max_length=50,unique=True)    
    name = models.CharField(max_length=50)    
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    width = models.FloatField()
    hight = models.FloatField()
    status = models.ForeignKey(ShipmentStatus,on_delete=models.CASCADE)
    receiver_date = models.DateField()
    estimated_dlivery_date = models.DateField()
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)



    def __str__(self):
        return f"{self.transfer_id}"

# def insert_initial_data(sender, created_models, **kwargs):
#     if ShipmentStatus in created_models:
#         for name in ('pending', 'complete', 'cancel'):
#             ShipmentStatus.objects.get_or_create(name=name.lower)

# post_migrate.connect(insert_initial_data)