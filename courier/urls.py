from django.urls import path
from courier.views import CourierListCreateApiView
app_name = "courier"



urlpatterns = [
    path("",CourierListCreateApiView.as_view(),name="index")
]