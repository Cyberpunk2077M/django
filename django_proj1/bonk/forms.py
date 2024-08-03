from django import forms
from .models import cartype

class cartypeForm(forms.Form):
    car_type= forms.ModelChoiceField(queryset=cartype.objects.all(), label='select_car_type')