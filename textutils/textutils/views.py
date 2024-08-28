from django.shortcuts import render
from django.http import HttpResponse 

def index(request):
    return render(request, 'index.html')

def analyze(request):
    textdjango=request.POST.get("text", 'Default Value')
    removepunc=request.POST.get("removepunc", 'off')
    capitalize=request.POST.get("capitalize", 'off')
    newlineremover= request.POST.get("newlineremover",'off')
    spaceremover= request.POST.get("spaceremover",'off')

    analyzed= ""

    if removepunc == "on":
        punctuations='''\!()-[]}{;:'""<,>/?@#$}%^&*~-_'''
        for char in textdjango:
            if char not in punctuations:
                analyzed= analyzed + char
        textdjango=analyzed
        
    if capitalize == "on":
        analyzed = textdjango.upper()
        textdjango=analyzed

    if newlineremover == "on":
        for char in textdjango:
            if char !="\n" and char != "\r":
                analyzed = analyzed + char
        textdjango=analyzed
    
    if spaceremover == "on":
        analyzed=""
        for index, char in enumerate(textdjango):
            if not(textdjango[index]==" " and textdjango[index+1]==" "):
                analyzed= analyzed + char
        textdjango=analyzed

    params= {'purpose':'removed puncs', 'analyzed_text': textdjango}
    return render(request, 'analyse.html', params)