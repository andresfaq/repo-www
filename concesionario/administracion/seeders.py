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
for x in range(60):
    Orden.save(OrdenFactory.create())


#Creando Vehiculos
for x in range(20):
    Vehiculo.save(VehiculoFactory.create())


#Creando Ventas
for x in range(50):
    Venta.save(VentaFactory.create())


#Creando RevisionVehiculo = #Ordenes
for x in range(60):
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
