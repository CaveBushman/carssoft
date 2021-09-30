from django.db import models
from drivers.models import Driver

from django.utils import timezone

# Create your models here.

class Car(models.Model):
    vin = models.CharField(max_length=19, verbose_name="VIN:")
    plate = models.CharField(max_length=10, verbose_name="RZ:")
    make = models.CharField(max_length=50, verbose_name="Výrobce")
    type= models.CharField(max_length=50, verbose_name="Typ")

    color = models.CharField(max_length=50, default="", verbose_name="Barva")

    stk_valid_to = models.DateField(null=True, verbose_name="STK platná do:")

    first_used_on_year = models.IntegerField(null=True, verbose_name="Rok uvedení do provozu")

    equipment = models.ManyToManyField('Equipment', blank=True, null=True)

    created = models.DateField(auto_now_add=True, blank=True)
    updated = models.DateField(auto_now=True, blank=True)

    def __str__(self):
        return f"{self.plate}, {self.make}"
        

class Equipment(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title