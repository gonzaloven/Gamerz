# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Producto
from django.views.generic import ListView
from django.shortcuts import render


# Create your views here.
class ProductoListView(ListView):
    queryset = Producto.objects.all()
    template_name = "productos/lista.html"


def producto_list_view(request):
    queryset = Producto.objects.all()
    context = {
        'lista_de_productos': querySet
    }
    return render(request, "productos/lista.html", context)
