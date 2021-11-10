from django.shortcuts import render, redirect
from django import forms
from Vehiculos.forms import VehiculoForm
from Vehiculos.models import Vehiculo
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def indexVehiculo(request):
    vehiculos= Vehiculo.objects.all()
    contexto = {
        'vehiculos':vehiculos
    }
    return render(request, 'index_vehiculo.html', contexto)

@login_required
def crearVehiculo(request):
    if request.method == 'GET':
        form = VehiculoForm()
        contexto = {
            'form':form
        }
    else: 
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index_vehiculo')
    return render(request, 'crear_vehiculo.html', {'form':form})

@login_required
def editarVehiculo(request, id):
    vehiculos = Vehiculo.objects.get(id = id)
    if request.method == 'GET':
        form = VehiculoForm(instance=vehiculos)
        contexto = {
            'form':form
        }
    else:
        form = VehiculoForm(request.POST,  instance= vehiculos)
        contexto={
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('index_vehiculo')
    return render(request, 'editar_vehiculo.html', contexto)

@login_required
def eliminarVehiculo(request, id):
    vehiculos = Vehiculo.objects.get(id = id)
    vehiculos.delete()
    return redirect('index_vehiculo')
