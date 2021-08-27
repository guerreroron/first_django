from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Estamos en la pagina del blog")

def first_blog(request):
    return HttpResponse("Este es mi primer blog escrito para django")

def second_blog(request):
    return HttpResponse("Hola esta ya es nuestra segunda entrada")


