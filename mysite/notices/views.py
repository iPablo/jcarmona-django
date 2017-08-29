from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#from . models import notice

# index con una pagina de inicio por defecto
def index(request):
    return HttpResponse("Hello, your are in the index notices")