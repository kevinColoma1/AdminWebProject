from django.shortcuts import render, redirect
from django import forms
from .forms import fields, ProveedorForm
from Proveedores.models import Proveedores
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def inicio(request):
    proveedores= Proveedores.objects.all()
    contexto = {
        'proveedores':proveedores
    }
    return render(request, 'index_proveedor.html', contexto)

@login_required
def crearProveedor(request):
    if request.method == 'GET':
        form = ProveedorForm()
        contexto = {
            'form':form
        }
    else: 
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index_proveedor')
    return render(request, 'crear_proveedor.html', {'form':form})

@login_required
def editarProveedor(request, Id):
    proveedores = Proveedores.objects.get(Id = Id)
    if request.method == 'GET':
        form = ProveedorForm(instance=proveedores)
        contexto = {
            'form':form
        }
    else:
        form = ProveedorForm(request.POST,  instance= proveedores)
        contexto={
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('index_proveedor')
    return render(request, 'editar_proveedor.html', contexto)

@login_required
def eliminarProveedor(request, Id):
    proveedores = Proveedores.objects.get(Id = Id)
    proveedores.delete()
    return redirect('index_proveedor')