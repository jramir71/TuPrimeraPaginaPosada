from django.urls import path
from home.views import inicio, crear_motocicletas, listado_motocicletas, detalle_motocicleta, VistaDetalleMotocicleta, VistaModificarMotocicleta, VistaEliminarMotocicleta

urlpatterns = [
    path('', inicio, name='inicio'),#las vistas son funciones que se ejecutan cuando se accede a una URL específica.
    path('motocicletas/', listado_motocicletas, name='listado_motocicletas'),
    path('motocicletas/crear/', crear_motocicletas, name='crear_motocicletas'),
    #path('motocicletas/<int:motocicleta_en_especifico>/', detalle_motocicleta, name='detalle_motocicletas'),
    path('motocicletas/<int:pk>/', VistaDetalleMotocicleta.as_view(), name='detalle_motocicletas'),
    path('motocicletas/<int:pk>/modificar/', VistaModificarMotocicleta.as_view(), name='modificar_motocicletas'),
    path('motocicletas/<int:pk>/eliminar/', VistaEliminarMotocicleta.as_view(), name='eliminar_motocicletas'),
    
] 