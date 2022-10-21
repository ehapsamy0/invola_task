from django.contrib import admin
from shipment.models import Shipment,ShipmentItem
# Register your models here.

admin.site.register(Shipment)
admin.site.register(ShipmentItem)