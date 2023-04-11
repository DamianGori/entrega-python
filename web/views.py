from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render
from miweb.models import productos
from miweb.forms import ProductosForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request, "index.html")

@login_required
def mis_productos(request):

    if request.method == "POST":
        productos_form = ProductosForm(request.POST)

        if productos_form.is_valid():
            data = productos_form.cleaned_data
            productos_data = productos(nombre_producto=data["nombre_producto"], precio_producto=data["precio_producto"], vencimiento_producto=data["vencimiento_producto"], descripcion_producto=data["descripcion_producto"])
            productos_data.save()
        return render(request, "mis_productos.html")

    productos_form = ProductosForm()
    return render(request, "mis_productos.html", {"forms":productos_form})
    

@login_required
def mostrar_productos(request):
    productos_objetos = productos.objects.all()
    contexto = {"productos_mostrar":productos_objetos}
    return render(request, "productos_agregados.html", contexto)


def eliminar_productos(request, id_delete):
    delete = productos.objects.get(id=id_delete)
    delete.delete()
    return render(request, "eliminar_productos.html")



@login_required
def ProductoDetalle(request):
    productos_objetos = productos.objects.all()
    contexto = {"productos_mostrar":productos_objetos}
    return render(request, "detalle_productos.html", contexto)



class EditarView(UpdateView):
    model = productos
    template_name = "edit_view.html"
    fields = ["nombre_producto", "precio_producto", "vencimiento_producto", "descripcion_producto"]
    print("Producto modificado")

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)