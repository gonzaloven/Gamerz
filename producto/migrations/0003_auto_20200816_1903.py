# Generated by Django 3.0.3 on 2020-08-16 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0002_producto_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='activo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='destacado',
            field=models.BooleanField(default=False),
        ),
    ]
