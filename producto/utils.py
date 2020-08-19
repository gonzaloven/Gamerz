import random
import string

from django.utils.text import slugify


def generadorStringRandom(size):
    caracteres = string.ascii_lowercase + string.digits
    return ''.join(random.choice(caracteres) for _ in range(size))


def generadorSlugUnico(instance, nuevoSlug=None):
    if nuevoSlug is not None:
        slug = nuevoSlug
    else:
        slug = slugify(instance.nombre)

    ProductoClass = instance.__class__

    existeClase = ProductoClass.objects.filter(slug=slug).exists()

    if existeClase:
        nuevoSlug = "{slug}-{randomString}".format(
            slug=slug,
            randomString=generadorStringRandom(size=4)
        )
        return generadorSlugUnico(instance, nuevoSlug=nuevoSlug)
    return slug

