from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Bienvenidos a la sección de deportes, puedes ingresar a first or second...")

def first_view(request):
    return HttpResponse("Noticias 1: Chile no va a ganar ninguna medalla...")

def another_first_view(request, my_val):
    return HttpResponse("Noticias 1: Chile no va a ganar ninguna medalla...  " + my_val)

def second_view(request):
    return HttpResponse("Noticias 2: China será el ganador de estos juegos olímpicos")

def another_second_view(request, tipo_indicador, year):
    return HttpResponse("Noticias 2: China será el ganador de estos juegos olímpicos " + tipo_indicador + " " +  str(year))

def third_view(request):
    return HttpResponse("Noticias 3: Un noruego batió su propio record mundial dos veces en los juegos olímpicos...")