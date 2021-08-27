"""django_intro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('first/', views.first_view),
    path('first/<str:my_val>', views.another_first_view),
    path('second/<str:tipo_indicador>/<int:year>', views.another_second_view),
    path('second/', views.second_view),
    path('second/<int:my_num>/<str:my_text>', views.another_second_view),
    path('third/', views.third_view),
]
