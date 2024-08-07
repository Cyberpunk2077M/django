from django import forms
from .models import Tweet

class Tweetform(forms.ModelForm):
    class Meta:
        model= Tweet
        fields= ['user', 'image', 'text']