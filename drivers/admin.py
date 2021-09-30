from django.contrib import admin
from django.contrib.admin.decorators import display
from .models import Address, Driver

# Register your models here.

class DriverAdmin(admin.ModelAdmin):
    readonly_fields =('driving_licence_valid_color',)

admin.site.register(Address)
admin.site.register(Driver, DriverAdmin)