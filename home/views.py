from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.forms import CreacionMotocicleta
from home.models import Motocicleta
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

def inicio(request):
    #return HttpResponse('<h1>Hola, esta es la página de inicio de mi proyecto Django</h1>')
    return render(request, 'home/inicio.html')

def crear_motocicletas(request):

    print('ESTOS SON LOS DATOS DEL GET ---->>', request.GET)
    print('ESTOS SON LOS DATOS DEL POST ---->>',request.POST)

    if request.method == 'POST':
        formulario = CreacionMotocicleta(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            motocicleta = Motocicleta(
                                      fecha_creacion=info.get('fecha_creacion'),
                                      marca=info.get('marca'), 
                                      linea=info.get('linea'), 
                                      modelo=info.get('modelo'), 
                                      placa=info.get('placa'),
                                      chasis=info.get('chasis'),
                                      motor=info.get('motor'),
                                      precio=info.get('precio')
                                      )
            motocicleta.save()
            return redirect('listado_motocicletas')
    else:
        formulario = CreacionMotocicleta()

    return render (request, 'home/crear_motocicletas.html', {'formulario': formulario})

def listado_motocicletas(request):
    motocicletas = Motocicleta.objects.all()
    return render(request, 'home/listado_motocicletas.html', {'motocicletas': motocicletas})

def detalle_motocicleta(request, motocicleta_en_especifico):
    motocicleta = Motocicleta.objects.get(id=motocicleta_en_especifico)
    return render(request, 'home/detalle_motocicleta.html', {'motocicleta':motocicleta})

class VistaDetalleMotocicleta (DetailView):
    model = Motocicleta
    template_name = 'home/detalle_motocicleta.html'

class VistaModificarMotocicleta (UpdateView):
    model = Motocicleta
    template_name = 'home/modificar_motocicleta.html'
    fields = ['fecha_creacion', 'marca', 'linea', 'modelo', 'placa', 'chasis', 'motor', 'precio']
    success_url = reverse_lazy('listado_motocicletas')

class VistaEliminarMotocicleta (DeleteView):
    model = Motocicleta
    template_name = 'home/eliminar_motocicleta.html'
    success_url = reverse_lazy('listado_motocicletas')