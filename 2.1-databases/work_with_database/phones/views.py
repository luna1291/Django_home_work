from django.http import HttpResponse
from django.shortcuts import render, redirect
from phones.models import Phone
from requests import request


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    if request.GET["sort"] == 'name':
        phones = Phone.objects.all().order_by("name")
    elif request.GET["sort"] == 'max_price':
        phones = Phone.objects.all().order_by('price')
    elif request.GET["sort"] == 'min_price':
        phones = Phone.objects.all().order_by('-price')
    else:
        phones = Phone.objects.all()    
    context = {
        "phones" : phones
    }
    return render(request, template, context)


def show_product(request, slug):
    phone = Phone.objects.get(slug = slug)
    template = 'product.html'
    context = {
       'phone' : phone,
    }
    return render(request, template, context)
