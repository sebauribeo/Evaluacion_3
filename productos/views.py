from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from productos.models import Productos
from productos.serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated

class TodosLosProductos(APIView):

    def get(self, request, *args, **kwargs):
        product = Productos.objects.all()
        serializer = ProductSerializer(product, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)    

class AgregarProducto(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        product = Productos.objects.all()
        serializer = ProductSerializer(product, many = True)
        total = len(serializer.data)
        return Response({'Message': {'Catidad de productos': total}}, status = status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'nombre': request.data.get('nombre'),
            'imagen': request.data.get('imagen'),
            'descripcion': request.data.get('descripcion'),
            'marca': request.data.get('marca'),
            'stock': request.data.get('stock'),
            'precio': request.data.get('precio'),
        }    

        serializer = ProductSerializer(data = data)
        if serializer.is_valid():
            if request.user.is_active == True:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({'Message': 'Debes estar autenticado para realizar esta operación'}, status=status.HTTP_401_UNAUTHORIZED)     
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
class ProductoPorId(APIView):

    permission_classes = [IsAuthenticated]

    def get_objects(self, id):
        res = Productos.objects.get(id=id)
        if res:
            return res
        else:
            return Response({'Message': 'Producto no existe'}, status=status.HTTP_400_BAD_REQUEST)
       
    def get(self, request, id_producto, *args, **kwargs):
        instancia_producto = Productos.objects.get(id = id_producto)
        print(instancia_producto)
        if instancia_producto:
            serializer = ProductSerializer(instancia_producto)
            return Response(serializer.data, status=status.HTTP_200_OK)  
        else:
            return Response({'Message': 'Producto no existe'}, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, id_producto, *args, **kwargs):
        instancia_producto = self.get_objects(id_producto)

        if not instancia_producto:
            return Response({'Message': 'Producto no existe'}, status = status.HTTP_400_BAD_REQUEST)
        data = {
            'nombre': request.data.get('nombre'),
            'imagen': request.data.get('imagen'),
            'descripcion': request.data.get('descripcion'),
            'marca': request.data.get('marca'),
            'stock': request.data.get('stock'),
            'precio': request.data.get('precio'),
        }   

        serializer = ProductSerializer(instance = instancia_producto, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id_producto, *args, **kwargs):
        instancia_producto = self.get_objects(id_producto)
        if not instancia_producto:
            return Response({"Message": "Producto no existe..."}, status=status.HTTP_400_BAD_REQUEST)
        instancia_producto.delete()
        return Response({"Message": "Producto eliminado..."}, status=status.HTTP_204_NO_CONTENT)
