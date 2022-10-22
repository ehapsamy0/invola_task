from urllib import response
from django.shortcuts import render,get_object_or_404
from rest_framework import status, generics
# Create your views here.
from shipment.models import Shipment,ShipmentStatus
from shipment.serializers import ShipmentSerializer
from rest_framework.response import Response



class ShipmentListCreateApiView(generics.ListCreateAPIView):
    serializer_class = ShipmentSerializer
    queryset = Shipment.objects.all()



class ShipmentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ShipmentSerializer


    def get_queryset(self):
        return Shipment.objects.all()



    def patch(self,request,pk,*args,**kwargs):
        new_status = request.data.get('status')
        if new_status:
            status_obj = get_object_or_404(ShipmentStatus,pk=new_status)
            shipment = get_object_or_404(Shipment,pk=pk)
            old_status = shipment.status
            if old_status.name == "cancel":
                if shipment.courier.can_canceld:
                    shipment.status = status_obj
                else:
                    message = {
                        "message":f"You can't canceld this shipment"} 
                    return Response(message,status=status.HTTP_400_BAD_REQUEST)
            else:
                shipment.status = status_obj
            message = {
                "message":f"Done Change  Status Form {old_status} to {status_obj} '_^ "
            }
            response_status = status.HTTP_200_OK
        else:
            message = {
                "message":f"Check Your Data This is not Status {new_status} "
            }
            response_status = status.HTTP_400_BAD_REQUEST
        return Response(message,status=response_status)
        

    def delete(self,request,pk,*args,**kwargs):
        message = {
            "message":"you did't have permission to do this '_^ "
        }
        return Response(message,status=status.HTTP_400_BAD_REQUEST)


    def put(self,request,pk,*args,**kwargs):
        message = {
            "message":"you did't have permission to do this '_^ "
        }
        return Response(message,status=status.HTTP_400_BAD_REQUEST)