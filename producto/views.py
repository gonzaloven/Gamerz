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
        return Producto.objects.todosLosProductos()


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


class ProductoDestacadoListView(ListView):
    template_name = "productos/list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Producto.objects.productosDestacados()


class ProductoDestacadoDetailView(DetailView):
    queryset = Producto.objects.productosDestacados()
    template_name = "productos/destacados-detail.html"