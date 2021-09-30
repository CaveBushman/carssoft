from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Driver

# Create your views here.

def DriversView(request):
    drivers = Driver.objects.all()
    data = {'drivers': drivers}
    return render (request, "drivers/drivers.html", data)


def DriverDetailView(request, pk):
    driver = get_object_or_404 (Driver, pk=pk)
    data = {'driver':driver}
    return render(request, "drivers/drivers-detail.html", data)