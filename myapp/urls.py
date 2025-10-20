from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('MisiónyVisión/', views.misionyvision, name='misionyvision'),
    path('¿PorqueOrionLegal?/', views.porqueorion, name='¿PorqueOrionLegal?'),
    path('¿QueBuscamos?/', views.quebuscamos, name='¿QueBuscamos?'),
    path('Login/', views.login, name='login'),
    path('Registro/', views.indexregistro, name='indexregistro'),
    path('RegistroCiudadano/', views.registrociudadano, name='registrociudadano'),
    path('RegistroAbogado/', views.registroabogado, name='registroabogado'),
]