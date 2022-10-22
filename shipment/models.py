from enum import unique
from operator import mod
import stat
from tokenize import blank_re
from django.db import models
from django.db.models.signals import pre_save,post_migrate,post_save
from courier.models import Courier

# Create your models here.
class ShipmentStatus(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return f"{self.name}"



def pre_save_set_defoult_status(sender,instance,*args, **kwargs):
    all_status = ShipmentStatus.objects.all()
    if len(all_status) < 2:
        defoult_status = ['pending','cancel','complete','awaiting_pickup',"in_way"]
        for status in defoult_status:
            ShipmentStatus.objects.get_or_create(name=status)


post_save.connect(pre_save_set_defoult_status,sender=ShipmentStatus)

class Shipment(models.Model):
    transfer_id = models.CharField(max_length=50,unique=True)
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)    
    reference1 = models.CharField(max_length=50,null=True,blank=True)
    reference2 = models.CharField(max_length=50,null=True,blank=True)
    reference3 = models.CharField(max_length=50,null=True,blank=True)
    origin_address = models.TextField(null=True,blank=True)
    origin_address_city = models.CharField(max_length=50)
    origin_address_state_or_province_code = models.CharField(max_length=50)
    origin_address_post_code = models.CharField(max_length=50)
    origin_address_country_code = models.CharField(max_length=50)
    destination_address = models.TextField(null=True,blank=True)
    destination_address_city = models.CharField(max_length=50)
    destination_address_state_or_province_code = models.CharField(max_length=50)
    destination_address_post_code = models.CharField(max_length=50)
    destination_address_country_code = models.CharField(max_length=50)
    number_of_pieces = models.IntegerField()
    actual_weight_unit = models.CharField(max_length=50)
    actual_weight_value = models.CharField(max_length=50)
    product_group = models.CharField(max_length=50)
    product_type = models.CharField(max_length=50)
    payment_type = models.CharField(max_length=50)
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