from dashboard import views
from django.urls import path
from . import views

urlpatterns = [

    path("", views.DriversView, name = "drivers-list"),
    path("/<int:pk>", views.DriverDetailView, name = "driver-detail")

]