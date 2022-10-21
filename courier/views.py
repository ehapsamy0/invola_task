from django.shortcuts import render
from rest_framework import status, generics
# Create your views here.

from courier.serializers import CourierSerializer




class CourierListCreateApiView(generics.ListCreateAPIView):
    serializer_class = CourierSerializer


    def get_queryset(self):
        queryset = Orders.objects.filter(active=False)
        return queryset
