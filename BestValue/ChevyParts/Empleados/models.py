from django.db import models
from django.db.models.deletion import CASCADE



# Create your models here.

class Cargo(models.Model):
    id = models.AutoField(primary_key=True)
    cargo = models.CharField(max_length=20)
    sueldo = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.cargo
    
    class Meta:
        db_table = 'empleados_cargo'

class Empleado(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=20)
    Apellido = models.CharField(max_length=20) 
    cargoEmpleado = models.ForeignKey(Cargo,null=True, blank=True, on_delete= models.CASCADE)
    
    def __str__(self):
        return self.Nombre

    class Meta:
        db_table = 'empleados_empleado'