from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from administracion.models import User, Empleado

@login_required
def inicio(request):
	return render(request, 'reportes/index.html')

@login_required
def usuarios(request):
	usuarios = User.objects.all()
	return render(request, 'reportes/usuarios.html',{'usuarios':usuarios})

@login_required
def inventario(request):
    return render(request, 'reportes/inventario.html')

@login_required
def ventas(request):
	usuarios = User.objects.all()
	return render(request, 'reportes/ventas.html',{'usuarios':usuarios})

# u1= User.objects.create(id='1', password='123456', last_login='2016-01-13', is_superuser='True', username='daniel', first_name='daniel', last_name='lopez', email='daniel@daniel.com',
#  is_staff='True', is_active='True', date_joined='2016-01-01', cedula='123456789', direccion='cra 123 # 123', fecha_de_nacimiento='1990-01-01', telefono='1234567')

# e1 = Empleado.objects.create(id_usuario='1',id_empleado="1",incio_contrato='2000-01-01', fin_contrato='2111-01-01',salario='9999999')

