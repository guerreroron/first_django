from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hola, bienvenidos a mi página... estas en la página principal")
