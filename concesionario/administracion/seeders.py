import autofixture
from django.contrib.auth.models import User
from administracion.models import *

suc = Sucursal.objects.all()
for x in suc:
    x.delete()

ven = Vendedor.objects.all()
for x in ven:
    x.delete()

ger = Gerente.objects.all()
for x in ger:
    x.delete()

emp = Empleado.objects.all()
for x in emp:
    x.delete()

usr = User.objects.all()
for x in usr:
    x.delete()

usuarios = autofixture.create('auth.User', 10)
for u in usuarios:
    User.objects._insert(u)

empleados = autofixture.create('administracion.Empleado', 10, follow_fk=True)
for e in empleados:
    Empleado.objects._insert(e)

sucursales= autofixture.create('administracion.Sucursal', 2)
for s in sucursales:
    Sucursal.objects._insert(s)

gerentes = autofixture.create('administracion.Gerente', 2, follow_fk=True)
for g in gerentes:
    Gerente.objects._insert(g)

vendedores = autofixture.create('administracion.Vendedor', 6, follow_fk=True)
for v in vendedores:
    Vendedor.objects._insert(v)

jefestaller = autofixture.create('administracion.JefeTaller', 2, follow_fk=True)
for jt in jefestaller:
    JefeTaller.objects._insert(jt)