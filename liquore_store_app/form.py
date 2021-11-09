from django import forms
from django.db import models
from django.forms import fields, widgets
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model=Cliente
        fields =[
            'nombre_cliente',
            'apellido',
            'email',
            'cedula',
            'telefono',
            'direccion',
        ]

        widgets = {
            'nombre_cliente' : forms.TextInput(attrs={'Placeholder':'Nombre'}),  
            'apellido' : forms.TextInput(attrs={'Placeholder':'Apellido'}), 
            'email' : forms.EmailInput(attrs={'Placeholder':'Email'}), 
            'cedula' : forms.NumberInput(attrs={'Placeholder':'Cedula'}), 
            'telefono' : forms.NumberInput(attrs={'Placeholder':'Telefono'}), 
            'direccion' : forms.TextInput(attrs={'Placeholder':'Direccion'}), 
        }