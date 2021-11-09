from django.db import models
from django.db.models.deletion import CASCADE
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import F, Sum, FloatField

User = get_user_model()
# Create your models here.

class CategoriaProd(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="categoriaProd"
        verbose_name_plural="categoriasProd"

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    categorias=models.ForeignKey(CategoriaProd, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='tienda')
    precio = models.FloatField()
    volumen = models.CharField(max_length=20)
    grados = models.CharField(max_length=10)
    descripcion = models.TextField()
    disponibilidad = models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="Producto"
        verbose_name_plural="Productos"

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    cliente_id=models.AutoField(auto_created=True, primary_key=True)
    nombre_cliente = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=25)
    cedula = models.IntegerField()
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=30)

    class Meta:
        verbose_name="Cliente"
        verbose_name_plural="Clientes"

    def __str__(self):
        return self.nombre_cliente + " " + self.apellido

class Order(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    fecha = models.DateTimeField(auto_now_add=True)

    @property
    def total(self):
        return self.orderline_set.aggregate(
            total=Sum(F("producto.precio") * F("cantidad"), output_field=FloatField())
        )["total"] or FloatField(0)

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'orders'
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['id']


class OrderLine(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cantidad} de {self.producto.nombre}'

    class Meta:
        db_table = 'orderlines'
        verbose_name = 'Línea de pedido'
        verbose_name_plural = 'Líneas de pedidos'
        ordering = ['id']

