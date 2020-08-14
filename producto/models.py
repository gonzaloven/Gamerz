# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField()
    precio = models.DecimalField(decimal_places=2, max_digits=20)

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre
