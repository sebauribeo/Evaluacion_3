from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Productos(models.Model):
    try:
        nombre = models.CharField(null = False, max_length = 100)
        imagen = models.CharField(null = False, max_length = 500)
        descripcion = models.CharField(null = False, max_length = 500)
        marca = models.CharField(null = False, max_length = 100)
        stock = models.IntegerField()
        precio = models.IntegerField()
        usuario = models.ForeignKey(User, on_delete=models.CASCADE, null = True)

        class Meta:
            ordering = ['id']

    except Exception as e:
        print('Modelo no creado: ', e)