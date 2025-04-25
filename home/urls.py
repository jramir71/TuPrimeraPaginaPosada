from django.urls import path
from home.views import inicio, crear_motocicletas

urlpatterns = [
    path('', inicio, name='inicio'),#las vistas son funciones que se ejecutan cuando se accede a una URL específica.
    path('motocicletas/crear/', crear_motocicletas, name='crear_motocicletas')
]