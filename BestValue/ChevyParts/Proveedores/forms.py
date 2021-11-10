from django import forms
from django.forms import fields
from .models import Proveedores

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedores
        fields = '__all__'