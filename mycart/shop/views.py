from django.shortcuts import render
from math import ceil
from.models import Product

# Create your views here.
def index(request):
    products=Product.objects.all()
    n=len(products)
    nslides=n//4 + ceil((n/4)+(n//4))
    params= {'no._of_slides':nslides, 'range': range(1,nslides),'product':products}
    return render(request, 'shop/index.html',params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return render(request, 'shop/contact.html')

def tracker(request):
    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')

def productView(request):
    return render(request, 'shop/productview.html')

def checkout(request):
    return render(request, 'shop/chekcout.html')