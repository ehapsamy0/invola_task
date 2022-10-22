
from os import stat
from rest_framework import serializers
from shipment.models import Shipment,ShipmentStatus
from courier.models import Courier
from courier.serializers import CourierSerializer



class StatusSipmentSerializer(serializers.ModelSerializer):


    class Meta:
        model = ShipmentStatus
        fields = "__all__"


class ShipmentSerializer(serializers.ModelSerializer):
    courier = serializers.SerializerMethodField(read_only=True)
    status = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Shipment
        fields = "__all__"


    def get_courier(self,obj):
        courier = obj.courier
        serializer = CourierSerializer(courier,many=False).data
        return serializer

    def get_status(self,obj):
        status = obj.status
        serializer = StatusSipmentSerializer(status,many=False).data
        return serializer