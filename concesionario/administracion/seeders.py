from django.contrib.auth.models import Group, Permission
from administracion.factories import SuperUserFactory, GerenteFactory, VendedorFactory, JefeTallerFactory, ClienteFactory, OrdenFactory, RepuestoFactory, RepuestosPorOrdenFactory, InventarioRepuestoFactory, VehiculoFactory, RevisionVehiculoFactory, InventarioVehiculoFactory, VentaFactory, CotizacionFactory
from administracion.models import User, Sucursal, Gerente, Vendedor, JefeTaller, Cliente, Orden, Repuesto, RepuestosPorOrden, InventarioRepuesto, Vehiculo, RevisionVehiculo, InventarioVehiculo, Venta, Cotizacion



#Eliminando Venta
vent = Venta.objects.all()
for x in vent:
    x.delete()

#Eliminando Cotizaciones
cot = Cotizacion.objects.all()
for x in cot:
    x.delete()


#Eliminando RevisionVehiculo
reveh = RevisionVehiculo.objects.all()
for x in reveh:
    x.delete()

#Eliminando Vehiculo
veh = Vehiculo.objects.all()
for x in veh:
    x.delete()

#Eliminando InventarioRepuestos
invrep = InventarioRepuesto.objects.all()
for x in invrep:
    x.delete()

#Eliminando repuestos por orden
repord = RepuestosPorOrden.objects.all()
for x in repord:
    x.delete()

#Eliminando Repuestos
rep = Repuesto.objects.all()
for x in rep:
    x.delete()

#Eliminando Ordenes
ord = Orden.objects.all()
for x in ord:
    x.delete()

#Eliminando Sucursales (las sucursales se crean al crear los gerentes)
suc = Sucursal.objects.all()
for x in suc:
    x.delete()

#Eliminando Clientes
usr = Cliente.objects.all()
for x in usr:
    x.delete()

#Eliminando Gerentes
usr = Gerente.objects.all()
for x in usr:
    x.delete()

#Eliminando Vendedores
usr = Vendedor.objects.all()
for x in usr:
    x.delete()

#Eliminando JefesTaller
usr = JefeTaller.objects.all()
for x in usr:
    x.delete()

#Eliminando Usuarios
usr = User.objects.all()
for x in usr:
    x.delete()

#eliminando grupos

grp = Group.objects.all()
for x in grp:
    x.delete()

print('DELETE COMPLETE')
#===================================================================================


#Creando superusuario
User.save(SuperUserFactory.create())

#Creando Clientes
for x in range(250):
    Gerente.save(ClienteFactory.create())

#Creando Gerentes
for x in range(3):
    Gerente.save(GerenteFactory.create())

#Creando Vendedores
for x in range(18):
    Vendedor.save(VendedorFactory.create())

#Creando JefesTaller
for x in range(6):
    JefeTaller.save(JefeTallerFactory.create())

#Creando Ordenes
for x in range(300):
    Orden.save(OrdenFactory.create())


#Creando Vehiculos
for x in range(20):
    Vehiculo.save(VehiculoFactory.create())


#Creando Ventas
for x in range(50):
    Venta.save(VentaFactory.create())


#Creando RevisionVehiculo = #Ordenes
for x in range(300):
    RevisionVehiculo.save(RevisionVehiculoFactory.create())

#Creando InventarioVehiculo = #Vehiculos
for x in range(20):
    InventarioVehiculo.save(InventarioVehiculoFactory.create())



#Creando Repuestos
for x in range(120):
    Repuesto.save(RepuestoFactory.create())

#Creando InventarioRepuesto = #Repuestos
for x in range(120):
    InventarioRepuesto.save(InventarioRepuestoFactory.create())

#Creando RepuestosPorOrden
for x in range(150):
    Repuesto.save(RepuestosPorOrdenFactory.create())

#Creando Cotizaciones
for x in range(50):
    Cotizacion.save(CotizacionFactory.create())

print('CREATE COMPLETE')

# Creacion y asignacion de grupos [falta asignar permisos por grupo]

grupo_gerentes = Group.objects.get_or_create(name='Gerentes')
grupo_vendedores = Group.objects.get_or_create(name='Vendedores')
grupo_jefestaller = Group.objects.get_or_create(name='JefesTaller')
grupo_clientes = Group.objects.get_or_create(name='Clientes')

clientes = Cliente.objects.all()
gerentes = Gerente.objects.all()
jefestaller = JefeTaller.objects.all()
vendedores = Vendedor.objects.all()

print('INICIANDO ASIGNACION DE GRUPOS')

for x in clientes:
    x.groups = [Group.objects.get(name='Clientes')]

for x in gerentes:
    x.groups = [Group.objects.get(name='Gerentes')]

for x in vendedores:
    x.groups = [Group.objects.get(name='Vendedores')]

for x in jefestaller:
    x.groups = [Group.objects.get(name='JefesTaller')]

print('GROUP COMPLETE')
