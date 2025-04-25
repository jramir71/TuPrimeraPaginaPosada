from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.forms import CreacionMotocicleta
from home.models import Motocicleta

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
            motocicleta = Motocicleta(marca=info.get('marca'), 
                                      linea=info.get('linea'), 
                                      modelo=info.get('modelo'), 
                                      placa=info.get('placa'),
                                      chasis=info.get('chasis'),
                                      motor=info.get('motor'),
                                      precio=info.get('precio')
                                      )
            motocicleta.save()
            return redirect('inicio')

    else:
        formulario = CreacionMotocicleta()

    return render (request, 'home/crear_motocicletas.html', {'formulario': formulario})