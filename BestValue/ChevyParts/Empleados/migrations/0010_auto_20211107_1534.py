# Generated by Django 3.2.7 on 2021-11-07 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Empleados', '0009_alter_empleado_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargo',
            name='cargo',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='Apellido',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='Nombre',
            field=models.CharField(max_length=20),
        ),
    ]