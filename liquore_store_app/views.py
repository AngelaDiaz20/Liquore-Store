from django import forms
from django.shortcuts import render
from . models import Producto, Cliente
from . carro import Carro
from django.shortcuts import redirect
from . form import ClienteForm
# Create your views here.

def index(request):

    return render(request, "liquore_store_app/index.html")   

def tienda(request):

    productos=Producto.objects.all()

    return render(request, "liquore_store_app/tienda.html", {"productos":productos})

def carrito(request):

    return render(request, "liquore_store_app/carrito.html")


def agregar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    return redirect("Tienda")

def agregar_producto_btn(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    return redirect("Carrito")

def eliminar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.eliminar_producto(producto=producto)
    return redirect("Carrito")

def restar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.restar_producto(producto=producto)
    return redirect("Carrito")

def limpiar_carro(request, producto_id):
    carro=Carro(request)
    carro.limpiar_carro()
    return redirect("Carrito")

def registro_datos(request):

    context ={}
    if request.method =="POST": 
        form = ClienteForm(request.POST)
        if form.is_valid():
            nombre_cliente=form.cleaned_data.get('nombre_cliente')
            apellido=form.cleaned_data.get('apellido')
            email=form.cleaned_data.get('email')
            cedula=form.cleaned_data.get('cedula')
            telefono=form.cleaned_data.get('telefono')
            direccion=form.cleaned_data.get('direccion')
            reg = Cliente.objects.create(
                nombre_cliente=nombre_cliente,
                apellido=apellido,
                email=email,
                cedula=cedula,
                telefono=telefono,
                direccion=direccion,
            )
            reg.save()
    else:
        form = ClienteForm()
    context['form'] = form

    return render(request, "liquore_store_app/registro_datos.html", context)


def datos_cliente(request):
    cliente=Cliente.objects.all()
    return render(request, "conf_pago.html",{"cliente" : cliente})

def resumen_pago(request):
    
    return render(request, "liquore_store_app/conf_pago.html")   

def politica_privacidad(request):
    
    return render(request, "liquore_store_app/polprivacidad.html")

def politica_entrega(request):
    
    return render(request, "liquore_store_app/polenvio.html")

def cuenta_regresiva(request):
    
    return render(request, "liquore_store_app/countdown.html")

def pago(request):
    
    pass
