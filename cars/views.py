from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def CarsView (request):
    return render (request, "cars/cars.html")