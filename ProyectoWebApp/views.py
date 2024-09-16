from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Home")

def servicios(request):
    return HttpResponse("servicios")

def tienda(request):
    return HttpResponse("tienda")

def blog(request):
    return HttpResponse("blog")

def contacto(request):
    return HttpResponse("contacto")

