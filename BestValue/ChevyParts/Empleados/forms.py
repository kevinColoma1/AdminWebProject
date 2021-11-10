from django import forms
from django.forms import  ModelForm
from Empleados.models import Cargo, Empleado
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group

class CargoForm(forms.ModelForm):
    class Meta:
        model= Cargo
        fields = "__all__"
        
class EmpleadosForm(forms.ModelForm):
    class Meta:
        model= Empleado
        fields = '__all__' 

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User.groups
        fields = ['username','first_name','last_name', 'email', 'group.name']
        labels = {'username':'Nombre de usuario','first_name':'Nombre','last_name':'Apellido', 'email':'Correo', 'group.name':'Grupos'}
        
        
