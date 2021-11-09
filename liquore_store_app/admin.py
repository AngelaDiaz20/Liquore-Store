from django.contrib import admin
from django.contrib.admin.decorators import register
from django.contrib.admin.options import ModelAdmin

from .models import CategoriaProd, Producto, Cliente, Order, OrderLine

# Register your models here.

class CategoriaProdAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")

    admin.site.register(CategoriaProd, CategoriaProdAdmin)
    admin.site.register(Producto)

class ClienteAdmin(admin.ModelAdmin):
    admin.site.register(Cliente)

class OrderAdmin(admin.ModelAdmin):
    admin.site.register(Order)

class OrderLineAdmin(admin.ModelAdmin):
    admin.site.register(OrderLine)

