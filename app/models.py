from django.db import models

# Create your models here.
class Cliente(models.Model):
        nro_doc = models.CharField(max_length=20, primary_key=True)
        tipo_doc = models.CharField(max_length=20)
        nombre_completo = models.CharField(max_length=50) 
        fecha_nac = models.DateField(max_length=20)                
        genero = models.CharField(max_length=20)
        telefono = models.IntegerField(max_length=20)
        email = models.EmailField(max_length=50)
        pasword = models.CharField(max_length=10)
        direccion = models.CharField(max_length=250) 
        ofertas = models.BooleanField(max_length=1)


class Tipo(models.Model):
        id = models.IntegerField(primary_key=True)
        descripcion = models.CharField(max_length=50)

        def __str__(self):
            return self.descripcion
        
    
class Porciones(models.Model):
        id = models.IntegerField(primary_key=True)
        cantidad = models.CharField(max_length=50) # 15 porc, 20 porc, 1 doc.
        precio = models.FloatField(max_length=20)
        cod_tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)


class Producto(models.Model):
        id = models.IntegerField(primary_key=True)
        nombre = models.CharField(max_length=50)
        descripcion = models.CharField(max_length=250)
        url = models.CharField(max_length=100)
        cod_tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)


class Pedido(models.Model):       
        fec_ing = models.DateField(max_length=20)
        direccion = models.CharField(max_length=250)
        fec_entrega = models.DateField(max_length=20)
        hora_entrega = models.CharField(max_length=10)        
        telefono = models.IntegerField(max_length=12) 
        nombre_completo = models.CharField(max_length=50)    #para compras sin registro          
        cod_cliente = models.ForeignKey(Cliente,blank=True, null=True, on_delete=models.CASCADE) #null para compras sin registro         


class Detalle(models.Model):        
        precio = models.FloatField(max_length=20)
        cod_prod = models.ForeignKey(Producto, on_delete=models.CASCADE)
        cantidad = models.IntegerField 
        cod_porciones = models.ForeignKey(Porciones, blank=True, null=True, on_delete=models.CASCADE)
        cod_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)






        
