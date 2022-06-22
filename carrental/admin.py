from django.contrib import admin

# Register your models here.
from .models import Vehicle,Manufacturer, Kind, VehicleInstance

admin.site.register(Vehicle)
admin.site.register(Manufacturer)
admin.site.register(Kind)
admin.site.register(VehicleInstance)