from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("hello, this is first homepage response for django project")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("hello, this is first about info response for django project")

def contact(request):
    return HttpResponse("hello, this is first contacts response for django project")