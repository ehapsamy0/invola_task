from django.urls import path
from shipment.views import ShipmentListCreateApiView,ShipmentRetrieveUpdateDestroyAPIView
app_name = "shipment"



urlpatterns = [
    path("",ShipmentListCreateApiView.as_view(),name="index"),
    path("<int:pk>/",ShipmentRetrieveUpdateDestroyAPIView.as_view(),name="change"),

]