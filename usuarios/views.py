from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import login as django_login 
from django.contrib import messages
from usuarios.forms import FormularioRegistro, FormularioEdicionPerfil
from django.contrib.auth.decorators import login_required
from usuarios.models import InfoExtra

def login(request):

    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            
            usuario = formulario.get_user()

            django_login(request, usuario)
            messages.success(request, f'Bienvenido {usuario.username}')

            InfoExtra.objects.get_or_create(user=usuario)  # Crear InfoExtra si no existe



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

@login_required
def editar_perfil(request):
    infoextra = request.user.infoextra
    if request.method == 'POST':
        formulario = FormularioEdicionPerfil(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            if formulario.cleaned_data['avatar']:
                infoextra.avatar = formulario.cleaned_data.get('avatar')
            infoextra.save()
            formulario.save()
            messages.success(request, 'Perfil actualizado correctamente')
            return redirect('inicio')
    else:
        formulario = FormularioEdicionPerfil(initial={'avatar':infoextra.avatar} ,instance=request.user)
    
    return render(request, 'usuarios/editar_perfil.html', {'formulario': formulario})