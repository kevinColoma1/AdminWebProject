"""ChevyParts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Proveedores.views import crearProveedor,editarProveedor,eliminarProveedor, inicio
from Empleados.views import editarEmpleado,inicio2, crearEmpleado, eliminarEmpleado, register
from Repuestos.views import crearRepuesto, editarRepuesto, repuesto, eliminarRepuesto
from Vehiculos.views import crearVehiculo, indexVehiculo, editarVehiculo, eliminarVehiculo
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, logout_then_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', LoginView.as_view(template_name = 'login.html'), name='login'),
    path('',inicio, name= 'index_proveedor' ),
    path('crear_proveedor', crearProveedor, name = 'crear_proveedor'),
    path('editar_proveedor/<int:Id>', editarProveedor, name = 'editar_proveedor'),
    path('eliminar_proveedor/<int:Id>', eliminarProveedor, name = 'eliminar_proveedor'),
    path('empleados/',inicio2, name='index_empleados' ),
    path('crear_empleados', crearEmpleado,  name='crear_empleados'),
    path('eliminarEmpleado/<int:id>',eliminarEmpleado, name ='Eliminar_empleado' ),
    path('editarEmpleado/<int:id>',editarEmpleado, name = 'editar_Empleado' ),
    path('repuestos/', repuesto, name ="index_repuesto"),
    path('crear_repuesto/', crearRepuesto, name ="crear_repuesto"),
    path('editar_repuestos/<int:id>', editarRepuesto, name ="editar_repuesto"),
    path('eliminar_repuestos/<int:id>', eliminarRepuesto, name ="eliminar_repuesto"),
    path('vehiculo/', indexVehiculo, name ="index_vehiculo"),
    path('crear_vehiculo/', crearVehiculo, name ="crear_vehiculo"),
    path('editar_vehiculo/<int:id>', editarVehiculo, name ="editar_vehiculo"),
    path('eliminar_vehiculo/<int:id>', eliminarVehiculo, name ="eliminar_vehiculo"),
    path('registro/',register, name='registro'),

  
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
