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


class ProductoDestacadoListView(ListView):
    template_name = "productos/list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Producto.objects.productosDestacados()


class ProductoDetailSlugView(DetailView):
    template_name = "productos/detail.html"

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')

        try:
            instanciaProducto = Producto.objects.get(slug=slug, active=True)
        except Producto.DoesNotExist:
            raise Http404("El producto solicitado no existe")
        except Producto.MultipleObjectsReturned:
            query = Producto.objects.filter(slug=slug, active=True)
            instanciaProducto = query.first()
        except:
            raise Http404("Oops")
        return instanciaProducto
