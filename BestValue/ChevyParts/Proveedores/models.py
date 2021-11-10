from django.db import models

# Create your models here.

class Proveedores(models.Model):
    Id = models.AutoField(primary_key=True)
    Razon_Social = models.CharField(max_length=100)
    Ruc = models.IntegerField(max_length=13)
    Teléfono = models.IntegerField (max_length=10)
    
    def __str__(self):
        return self.Razon_Social