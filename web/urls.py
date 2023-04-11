"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from web.views import inicio, mis_productos, mostrar_productos, eliminar_productos, EditarView, ProductoDetalle
from miweb.forms import ProductosForm
from login.views import login_request, register, logout_request, EditarPerfil
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", inicio),
    path("mis_productos", mis_productos, name="productos"),
    path("productos_agregados", mostrar_productos, name="misproductos"),
    path("productos_detalle", ProductoDetalle, name="detalle"),
    path("eliminar_productos/<id_delete>/", eliminar_productos, name="eliminar"),
    path("edit_view/<pk>", EditarView.as_view(), name="EditarView"),
    path("login", login_request, name="login"),
    path("register", register, name="register"),
    path("logout", logout_request, name="logout"),
    path("editar_usuario", EditarPerfil, name="EditarPerfil")
]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)