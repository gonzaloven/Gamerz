# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Producto
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.http import Http404


# Create your views here.
class ProductoListView(ListView):
    queryset = Producto.objects.all()
    template_name = "productos/list.html"


def producto_list_view(request):
    queryset = Producto.objects.all()
    context = {
        'lista_de_productos': querySet
    }
    return render(request, "productos/list.html", context)


class ProductoDetailView(DetailView):
    queryset = Producto.objects.all()
    template_name = "productos/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductoDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context


def producto_detail_view(request, pk=None, *args, **kwargs):
    queryset = Producto.objects.filter(id=pk)
    if queryset.exists() and queryset.count() == 1:
        instance = queryset.first()
    else:
        raise Http404("El producto solicitado no existe")

    context = {
        'object': instance
    }
    return render(request, "productos/detail.html", context)
