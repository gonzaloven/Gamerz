# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import random
from django.db import models


# Create your models here.

def uploadImagePath(instance, filename):
    return os.path.join('productos', str(instance.id), filename)


class ProductoManager(models.Manager):
    def buscarProductoPorId(self, idProducto):
        queryset = self.get_queryset().filter(id=idProducto)
        if queryset.count() == 1:
            return queryset.first()
        return None


class Producto(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField()
    precio = models.DecimalField(decimal_places=2, max_digits=20)
    imagen = models.ImageField(upload_to=uploadImagePath, null=True, blank=True)

    objects = ProductoManager()

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre
