from django import forms

class CreacionMotocicleta(forms.Form):
    marca = forms.CharField(max_length=100, label='Marca')
    linea = forms.CharField(max_length=100, label='Línea')
    modelo = forms.IntegerField(label='Modelo')
    placa = forms.CharField(max_length=100, label='Placa')
    chasis = forms.CharField(max_length=100, label='Chasis')
    motor = forms.CharField(max_length=100, label='Motor')
    precio = forms.DecimalField(max_digits=10, decimal_places=2, label='Precio')