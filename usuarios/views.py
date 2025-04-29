from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as django_login 
from django.contrib import messages
from usuarios.forms import FormularioRegistro

def login(request):

    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            
            usuario = formulario.get_user()

            django_login(request, usuario)
            messages.success(request, f'Bienvenido {usuario.username}')

            return redirect('inicio')
        
    
    else: 
        formulario = AuthenticationForm()

    return render(request, 'usuarios/login.html', {'formulario': formulario})

def registro(request):
    if request.method == 'POST':
        formulario = FormularioRegistro(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Usuario creado correctamente')
            return redirect('login')
    else:
        formulario = FormularioRegistro()
    
    return render(request, 'usuarios/registro.html', {'formulario': formulario})