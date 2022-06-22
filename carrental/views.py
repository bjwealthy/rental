from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Vehicle, Kind, Manufacturer, VehicleInstance

def index(request):
    """view function for the app homepage"""
    num_vehicle=Vehicle.objects.all().count()
    num_vehicle_instance = VehicleInstance.objects.all().count()
    num_instances_available=VehicleInstance.objects.filter(status='a').count()
    num_manufacturers=Manufacturer.objects.count()

    context={
        'num_vehicle': num_vehicle,
        'num_vehicle_instance': num_vehicle_instance,
        'num_instances_available': num_instances_available
    }
    return render(request, 'index.html', context=context)