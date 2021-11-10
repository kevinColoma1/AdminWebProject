from django.db import models

# Create your models here.

class Vehiculo(models.Model):
    id = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=45)
    modelo = models.CharField(max_length=45)
    año = models.IntegerField(max_length=11)

    def __str__(self):
        return '%s - %s - %s' % (self.marca,  self.modelo, self.año)