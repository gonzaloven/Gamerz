# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Producto
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.http import Http404


# Create your views here.
class ProductoListView(ListView):
    template_name = "productos/list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Producto.objects.all()


def producto_list_view(request):
    queryset = Producto.objects.all()
    context = {
        'lista_de_productos': querySet
    }
    return render(request, "productos/list.html", context)


class ProductoDetailView(DetailView):
    template_name = "productos/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductoDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Producto.objects.buscarProductoPorId(pk)
        if instance is None:
            raise Http404("El producto solicitado no existe")
        return instance


def producto_detail_view(request, pk=None, *args, **kwargs):
    instance = Producto.objects.buscarProductoPorId(pk)
    if instance is None:
        raise Http404("El producto solicitado no existe")

    context = {
        'object': instance
    }
    return render(request, "productos/detail.html", context)


class ProductoDestacadoListView(ListView):
    template_name = "productos/list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Producto.objects.productosDestacados()


class ProductoDestacadoDetailView(DetailView):
    queryset = Producto.objects.productosDestacados()
    template_name = "productos/destacados-detail.html"