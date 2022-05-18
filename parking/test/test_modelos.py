from django.test import TestCase
from parking.models import Cliente,Plaza,Dimensiones

#Cliente creado correctamente
class ClienteTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        Dimensiones.objects.create(tipo='prueba',altura=2,anchura=2,largura=2)
        dimPrueba = Dimensiones.objects.get(tipo='prueba')
        Plaza.objects.create(planta=1,numero=1,dimensiones=dimPrueba)
        plaza1= Plaza.objects.get(numero=1)
        Cliente.objects.create(dni='73012345H', nombre='Sergio',apellidos='Soteras Serrano',vehiculo='C4',plaza = plaza1)
        Cliente.objects.create(dni='73543210H', nombre='Robustiano',apellidos='Rios Gil',vehiculo='Focus',)

    def test_str_cliente(self):
       cliente = Cliente.objects.get(dni='73012345H')
       self.assertEqual(cliente.__str__(),'Sergio Soteras Serrano')
       self.assertEqual(cliente.vehiculo,'C4')

    def test_cliente_plaza(self):
        cliente = Cliente.objects.get(dni='73012345H')
        self.assertEqual(cliente.plaza,Plaza.objects.get(numero=1))

#Cliente modificado correctamente
    def test_modificar_cliente(self):
        cliente = Cliente.objects.get(dni='73012345H')
        cliente.nombre = 'Pedro'
        cliente.save()
        self.assertEqual(Cliente.objects.get(dni='73012345H').nombre,'Pedro')

#Cliente eliminado correctamente
    def test_eliminar_cliente(self):
        cliente = Cliente.objects.get(dni='73012345H')
        cliente.delete()
        self.assertEqual(Cliente.objects.first().nombre,'Robustiano')
        

#Plaza creada correctamente
class PlazaTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        Dimensiones.objects.create(tipo='prueba',altura=2,anchura=2,largura=2)
        dimPrueba = Dimensiones.objects.get(tipo='prueba')
        Plaza.objects.create(planta=1,numero=1,dimensiones=dimPrueba)
        plaza1= Plaza.objects.get(numero=1)
        Cliente.objects.create(dni='73012345H', nombre='Sergio',apellidos='Soteras Serrano',vehiculo='C4',)

    def test_plaza_creada_correctamente(self):
       plaza1= Plaza.objects.get(numero=1)
       self.assertEqual(plaza1.planta,1)

    def test_plaza_dimensiones(self):
        plaza1=Plaza.objects.get(numero=1)
        self.assertEqual(plaza1.dimensiones,Dimensiones.objects.get(tipo='prueba'))

    def test_str_plaza(self):
        plaza1=Plaza.objects.get(numero=1)
        self.assertEqual(plaza1.__str__(),'Plaza 1 ( Planta 1 )')
#Plaza disponible
    def test_plaza_disponible(self):
        plaza1= Plaza.objects.get(numero=1)
        self.assertTrue(plaza1.disponible())
        cliente = Cliente.objects.get(dni='73012345H')
        cliente.plaza = plaza1
        cliente.save()
        self.assertFalse(plaza1.disponible())

#Cliente de la plaza
    def test_plaza_cliente(self):
        plaza1= Plaza.objects.get(numero=1)
        cliente = Cliente.objects.get(dni='73012345H')
        cliente.plaza = plaza1
        cliente.save()
        self.assertEqual(plaza1.nombre_cliente(),cliente)

#Dimensiones creada correctamente
class DimensionesTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        Dimensiones.objects.create(tipo='prueba',altura=2,anchura=2,largura=2)

    def test_dimensiones_creada(self):
        dim = Dimensiones.objects.get(tipo='prueba')
        self.assertEqual(dim.altura,2)
        self.assertEqual(dim.anchura,2)
        self.assertEqual(dim.largura,2)
    
    def test_str_dimensiones(self):
        dim = Dimensiones.objects.get(tipo='prueba')
        self.assertEqual(dim.__str__(),'prueba (2.00m x 2.00m x 2m)')