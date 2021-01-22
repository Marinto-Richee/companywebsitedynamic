from django.shortcuts import render
from .models import people,product
# Create your views here.


def home(request):
    context = {}
    return render(request, 'spldynamic/home.html', context)

def pro(request):
    context = {}
    context["products"]= product.objects.all()  
    return render(request, 'spldynamic/product.html', context)

def ppl(request):
    context = {}
    context["ppls"]= people.objects.all()  
    return render(request, 'spldynamic/people.html', context)
    
def contact(request):
    context = {}
    return render(request, 'spldynamic/contactus.html', context)
