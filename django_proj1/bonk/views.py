from django.shortcuts import render
from .models import cartype
# Create your views here.
def bonkfn1(request):
    cars = cartype.objects.all()
    return render(request, 'bonk/index_bonk.html', {'cars': cartype})
