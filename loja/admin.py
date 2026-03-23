from django.contrib import admin
from .models import *

# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "morada")
    ordering =("name",)
    search_fields =("name",)

admin.site.register(Cliente,ClienteAdmin)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("name",)
    ordering =("name",)
    search_fields =("name",)

admin.site.register(Categoria,CategoriaAdmin)

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("name","categoria")
    ordering =("name",)
    search_fields =("name",)

admin.site.register(Produto,ProdutoAdmin)

class PedidoAdmin(admin.ModelAdmin):
    list_display = ("id","cliente")
    ordering =("cliente",)
    search_fields =("cliente",)

admin.site.register(Pedido,PedidoAdmin)

class ItemAdmin(admin.ModelAdmin):
    list_display = ("produto", "quantidade")
    ordering =("quantidade",)
    search_fields =("produto",)

admin.site.register(Pedido,PedidoAdmin)