from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'blog/index.html')

def about(request):
    return HttpResponse("This is about page")

def contact(request):
    return HttpResponse("This is Contact Us page")

def search(request):
    return HttpResponse("This is search page")

def related(request):
    return HttpResponse("This is related blog page")

def dashboard(request):
    return HttpResponse("This is dashboard page")

def community(request):
    return HttpResponse("This is Community page")