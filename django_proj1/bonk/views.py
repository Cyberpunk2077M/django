from django.shortcuts import render
from .models import cartype
from django.shortcuts import get_object_or_404

def bonkfn1(request):
    cars = cartype.objects.all()
    return render(request, 'bonk/index_bonk.html', {'cartype': cars})

def car_details(request, car_id):
    car = get_object_or_404(cartype, pk=car_id)
    return render(request, 'bonk/cardetail.html', {'car': car, 'car_id': car_id})