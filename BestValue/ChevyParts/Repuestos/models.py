from django.db import models
from django.db.models.deletion import CASCADE
from Empleados.models import Empleado
from Proveedores.models import Proveedores

from Vehiculos.models import Vehiculo
from .choices import descripcion
# Create your models here.
class Repuesto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_repuesto = models.CharField(max_length=45)
    Descripcion = models.CharField(max_length=1, choices= descripcion, default='O')
    Fk_vehiculo = models.ForeignKey(Vehiculo, null=True, blank=True, on_delete= models.CASCADE)
    Fk_proveedor = models.ForeignKey(Proveedores, null = True, blank= True, on_delete=CASCADE)
    
    