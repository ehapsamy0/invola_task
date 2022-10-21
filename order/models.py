from operator import mod
from django.db import models

from courier.models import Courier
from shipment.models import Shipment

# Create your models here.


class OrderStatus(models.Model):
    name = models.CharField(max_length=100)

class Order(models.Model):
    transfer_id = models.CharField(max_length=50,unique=True)
    courier = models.ForeignKey(Courier,on_delete=models.CASCADE)
    shipment = models.ForeignKey(Shipment,on_delete=models.CASCADE)
    status = models.ForeignKey(OrderStatus,on_delete=models.CASCADE)
    receiver_date = models.DateField()
    estimated_dlivery_date = models.DateField()
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
