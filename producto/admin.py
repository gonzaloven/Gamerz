# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Producto
from django.contrib import admin


# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']

    class Meta:
        model = Producto


admin.site.register(Producto, ProductoAdmin)
