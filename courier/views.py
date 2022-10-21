from django.shortcuts import render
from rest_framework import status, generics
# Create your views here.
from courier.models import Courier
from courier.serializers import CourierSerializer




class CourierListCreateApiView(generics.ListCreateAPIView):
    serializer_class = CourierSerializer


    def get_queryset(self):
        queryset = Courier.objects.filter(active=True)
        return queryset



class CourierRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CourierSerializer


    def get_queryset(self):
        queryset = Courier.objects.filter(active=True)
        return queryset
