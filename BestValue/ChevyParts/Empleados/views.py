from django import forms
from django.contrib.auth.models import Group, User
from .forms import EmpleadosForm,CargoForm, UserCreationForm
from django.shortcuts import render, redirect
from Empleados.models import Empleado, Cargo
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.template import RequestContext

from django.views.generic import CreateView, TemplateView



@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
           post = form.save(commit= False)
           group_name = request.POST.get('group_name')
           g = Group.objects.get(name = group_name)
           g.user_set.add(User)
           post.save()
           return redirect('index_repuesto', pk= post.pk)
    else:
        form = UserCreationForm()
        groups= Group.objects.all()
        
    return render (request, 'register.html', {'form':form, 'groups':groups}, context_instance = RequestContext(request))

# Create your views here.

@login_required
def inicio2(request):
    empleados = Empleado.objects.all()
    contexto={
        'empleados' : empleados
    }
    return render(request, 'index_empleados.html', contexto)

@login_required
def crearEmpleado(request):
    if request.method == 'GET':

        form = EmpleadosForm()
        contexto = {
            'form':form
        }
    else:
        form= EmpleadosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('index_empleados')
    return render (request, 'crear_empleados.html', {"form":form} )

@login_required
def crearCargo(request):
    if request.method == 'GET':
        form = CargoForm()
        contexto = {
            'form': form
        }
    else:
        form= CargoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index_empleados')
    return render(request, 'crear_cargo.html', contexto)

@login_required
def editarEmpleado(request, id):
    empleados = Empleado.objects.get(id = id)
    if request.method == 'GET':
        form = EmpleadosForm(instance=empleados)
        contexto = {
            'form':form
        }
    else:
        form = EmpleadosForm(request.POST, instance=empleados)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('index_empleados')
    return render(request, 'editar_empleado.html',contexto)


@login_required
def eliminarEmpleado(request, id ):
    empleados = Empleado.objects.get(id = id)
    empleados.delete()
    return redirect('index_empleados')