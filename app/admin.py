from django.contrib import admin

# Register your models here.

from .models import Cliente, Tipo, Porciones, Producto, Pedido, Detalle


#metodo que me permite listar todos los productos en admin
class ClienteAdmin(admin.ModelAdmin):
      list_display=("nro_doc","tipo_doc","nombre_completo","fecha_nac","genero","telefono","email","pasword","direccion","ofertas")
      search_fields=("nro_doc",)
      list_filter=("tipo_doc",)  

class TipoAdmin(admin.ModelAdmin):
      list_display=("id","descripcion")
      search_fields=("id",)
      list_filter=("descripcion",)  

class PorcionesAdmin(admin.ModelAdmin):
      list_display=("id","cantidad","precio","cod_tipo")
      search_fields=("id",)
      list_filter=("cod_tipo",) 

class ProductoAdmin(admin.ModelAdmin):
      list_display=("id","nombre","descripcion","url","cod_tipo")
      search_fields=("id",)
      list_filter=("cod_tipo",) 

class PedidoAdmin(admin.ModelAdmin):
      list_display=("id","fec_ing","direccion","fec_entrega","hora_entrega","telefono","Recibe_nombre","cod_cliente")
      search_fields=("id",)
      date_hierarchy="fec_entrega"

class DetalleAdmin(admin.ModelAdmin):
      list_display=("id","cod_prod","cant","cod_porciones","cod_pedido")
      search_fields=("cod_prod",)
      list_filter=("cod_pedido",) 


#class PromocionesAdmin(admin.ModelAdmin):
 #  list_display=("id","fec_ini","fec_fin","por_des","canal_atencion")
  #  list_filter=("fec_ini",)  #filtrar en una lista por fecha
   # date_hierarchy="fec_ini"  #filtrar en un menu por mes


#registramos las clases en admin
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Tipo, TipoAdmin)
admin.site.register(Porciones, PorcionesAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Detalle, DetalleAdmin)