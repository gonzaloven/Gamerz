# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import random
from django.db import models
from django.db.models.signals import pre_save
from .utils import generadorSlugUnico

# Create your models here.



def uploadImagePath(instance, filename):
    return os.path.join('productos', str(instance.id), filename)


class ProductoQuerySet(models.query.QuerySet):
    def activos(self):
        return self.filter(activo=True)

    def destacados(self):
        return self.filter(destacado=True, activo=True)


class ProductoManager(models.Manager):
    def get_queryset(self):
        return ProductoQuerySet(self.model, using=self._db)

    def todosLosProductos(self):
        return self.get_queryset().activos()

    def productosDestacados(self):
        return self.get_queryset().destacados()

    def buscarProductoPorId(self, idProducto):
        queryset = self.get_queryset().filter(id=idProducto)
        if queryset.count() == 1:
            return queryset.first()
        return None

    def delete(self):
        return self.todosLosProductos().delete()


class Producto(models.Model):
    nombre = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, unique=True)
    descripcion = models.TextField()
    precio = models.DecimalField(decimal_places=2, max_digits=20)
    imagen = models.ImageField(upload_to=uploadImagePath, null=True, blank=True)
    activo = models.BooleanField(default=True)
    destacado = models.BooleanField(default=False)

    objects = ProductoManager()

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre


def agregarSlug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = generadorSlugUnico(instance)


pre_save.connect(agregarSlug, sender=Producto)