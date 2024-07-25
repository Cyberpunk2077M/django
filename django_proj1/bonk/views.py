from django.shortcuts import render

# Create your views here.
def bonkfn1(request):
    return render(request, 'bonk/index_bonk.html')