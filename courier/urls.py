from django.urls import path
from courier.views import CourierListCreateApiView,CourierRetrieveUpdateDestroyAPIView
app_name = "courier"



urlpatterns = [
    path("",CourierListCreateApiView.as_view(),name="index"),
    path("<int:pk>/",CourierRetrieveUpdateDestroyAPIView.as_view(),name="change"),

]