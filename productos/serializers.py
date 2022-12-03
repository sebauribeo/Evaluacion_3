from rest_framework import serializers
from .models import Productos

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Productos
        fields = ['id', 'nombre', 'imagen', 'descripcion', 'marca', 'stock', 'precio', 'usuario']