from django.shortcuts import render
from .models import cartype, dealership
from django.shortcuts import get_object_or_404
from .forms import cartypeForm

def bonkfn1(request):
    cars = cartype.objects.all()
    return render(request, 'bonk/index_bonk.html', {'cartype': cars})

def car_details(request, car_id):
    car = get_object_or_404(cartype, pk=car_id)
    return render(request, 'bonk/cardetail.html', {'car': car, 'car_id': car_id})

def company(request, company, model_name):
    comp=get_object_or_404(cartype, brand=company, name=model_name)
    return render(request, 'bonk/company.html',{'comp': comp,})

def cardealer_view(request):
    dealers=None
    if request.method == 'POST':
        form= cartypeForm(request.POST)
        if form.is_valid():
            car_type= form.cleaned_data['car_type']
            dealers= dealership.objects.filter(carname=car_type)
    else:
        form= cartypeForm()
    return render(request,'bonk/cardealer.html', {'dealers':dealers, 'form':form})
