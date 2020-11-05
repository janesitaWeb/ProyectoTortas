from django.test import TestCase
from app.models import Tipo, Porciones


class PorcionesTestCase(TestCase):
     def setUp(self):
        tipo1 = Tipo.objects.create(id=7,descripcion="tapaditos")
        Porciones.objects.create(id = 3, cantidad ="12 unidades",precio=6000,cod_tipo=tipo1)


def test_porciones_tipo(self):
      Porciones1 = Porciones.objects.get(id=3)
      self.assertEqual(Porciones1.cod_tipo.descripcion,"tapaditos")  

def test_porciones_precio(self):
       Porciones2 = Porciones.objects.get(id=3)
       self.assertEqual(Porciones2.precio*2,12000)

