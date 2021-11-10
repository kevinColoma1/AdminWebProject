from django import forms
from django.forms import fields
from .models import Repuesto

class RepuestoForm(forms.ModelForm):
    class Meta:
        model = Repuesto
        fields = '__all__'