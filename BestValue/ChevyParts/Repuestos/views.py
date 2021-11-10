from django.shortcuts import render, redirect
from .forms import RepuestoForm
from Repuestos.models import Repuesto
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def repuesto(request):
    repuestos= Repuesto.objects.all()
    contexto = {
        'repuestos':repuestos
    }
    return render(request, 'index_repuesto.html', contexto)

@login_required
def crearRepuesto(request):
    if request.method == 'GET':
        form = RepuestoForm()
        contexto = {
            'form':form
        }
    else: 
        form = RepuestoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index_repuesto')
    return render(request, 'crear_repuesto.html', {'form':form})

@login_required
def editarRepuesto(request, id):
    repuestos = Repuesto.objects.get(id = id)
    if request.method == 'GET':
        form = RepuestoForm(instance=repuestos)
        contexto = {
            'form':form
        }
    else:
        form = RepuestoForm(request.POST,  instance= repuestos)
        contexto={
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('index_repuesto')
    return render(request, 'editar_repuesto.html', contexto)


@login_required
def eliminarRepuesto(request, id):
    repuestos = Repuesto.objects.get(id = id)
    repuestos.delete()
    return redirect('index_repuesto')
