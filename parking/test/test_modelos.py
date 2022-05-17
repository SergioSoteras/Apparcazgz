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
       self.assertEquals(plaza1.planta,1)

#Plaza disponible
    def test_plaza_disponible(self):
        plaza1= Plaza.objects.get(numero=1)
        self.assertTrue(plaza1.disponible())
        cliente = Cliente.objects.get(dni='73012345H')
        cliente.plaza = plaza1
        cliente.save()
        self.assertFalse(plaza1.disponible())
