from django.db import models

# Create your models here.
class Productos(models.Model):
    try:
        nombre = models.CharField(null = False, max_length = 100)
        imagen = models.CharField(null = False, max_length = 500)
        descripcion = models.CharField(null = False, max_length = 500)
        marca = models.CharField(null = False, max_length = 100)
        stock = models.IntegerField()
        precio = models.IntegerField()

        class Meta:
            ordering = ['id']

    except Exception as e:
        print('Modelo no creado: ', e)