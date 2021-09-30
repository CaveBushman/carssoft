from dashboard import views
from django.urls import path
from . import views


urlpatterns = [
    path("", views.CarsView, name = "cars-list")
]