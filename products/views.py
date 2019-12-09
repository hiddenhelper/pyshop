from django.http import  HttpResponse
from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.Objects.all()
    return render(request, 'index.html', {'products': products})

def new(request):
    return HttpResponse('new World')