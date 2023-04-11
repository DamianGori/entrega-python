from django import forms

class ProductosForm(forms.Form):
    nombre_producto = forms.CharField(max_length=25)
    precio_producto = forms.IntegerField()
    vencimiento_producto = forms.DateField()
    descripcion_producto = forms.CharField(max_length=60)