# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Producto
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404


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


class ProductoDetailView(DetailView):
    queryset = Producto.objects.all()
    template_name = "productos/detalles.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductoDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context


def producto_detail_view(request, pk=None, *args, **kwargs):
    instance = get_object_or_404(Producto, pk=pk)
    context = {
        'object': instance
    }
    return render(request, "productos/detalles.html", context)
