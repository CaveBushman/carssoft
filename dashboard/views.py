from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def dashboardView(request):
    print ("voláš funkci dashboard")
    return render (request, "dashboard/dashboard.html")