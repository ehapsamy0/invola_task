from django.contrib import admin
from shipment.models import Shipment,ShipmentStatus
# Register your models here.

admin.site.register(Shipment)
admin.site.register(ShipmentStatus)