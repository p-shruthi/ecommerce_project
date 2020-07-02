from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    #return HttpResponse("Hello! This is E-Commerce Index page :")
    return render(request, 'django_ecommerce_app/index.html')


def shop(request):
    return render(request, 'django_ecommerce_app/home.html')