from django.db import models
from django.utils import timezone

# Create your models here.


class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip = models.CharField(max_length=10)
    state = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.city}, {self.street}"


class Driver (models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField
    personal_identification_number = models.IntegerField()

    image = models.ImageField(null=True, blank=True, upload_to = "static/images/drivers")

    email = models.EmailField(max_length=100, null=True)
    tel = models.CharField(max_length=13)

    driving_licence_no = models.CharField(max_length=20)
    driving_licence_issued = models.CharField(max_length=50)
    driving_licence_class_A = models.BooleanField(default=False)
    driving_licence_class_B = models.BooleanField(default=False)
    driving_licence_class_C = models.BooleanField(default=False)
    driving_licence_class_D = models.BooleanField(default=False)
    driving_licence_class_E = models.BooleanField(default=False)
    driving_licence_class_T = models.BooleanField(default=False)
    driving_licence_valid_to = models.DateField(null=True)

    driving_licence_valid_color = models.CharField(max_length=50, default="green")

    address = models.ForeignKey (Address, on_delete = models.SET_NULL, null=True)

    created = models.DateField(auto_now_add=True, blank=True)
    updated = models.DateField(auto_now=True, blank=True)

    def __str__ (self):
        return f"{self.first_name} {self.last_name}"
