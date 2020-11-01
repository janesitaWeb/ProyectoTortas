from django.contrib import admin

# Register your models here.

from .models import Cliente, Tipo, Porciones, Producto, Pedido, Detalle


#metodo que me permite listar todos los productos en admin
#class ProductoAdmin(admin.ModelAdmin):
 #   list_display=("id","nombre","especificacion","precio_venta","stock_total","tipo")
  #  search_fields=("id",)


#class PromocionesAdmin(admin.ModelAdmin):
 #  list_display=("id","fec_ini","fec_fin","por_des","canal_atencion")
  #  list_filter=("fec_ini",)  #filtrar en una lista por fecha
   # date_hierarchy="fec_ini"  #filtrar en un menu por mes


#registramos las clases en admin
admin.site.register(Cliente)
admin.site.register(Tipo)
admin.site.register(Porciones)
admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(Detalle)