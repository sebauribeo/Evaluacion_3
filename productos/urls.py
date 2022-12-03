from django.urls import path
from .views import TodosLosProductos, ProductoPorId, AgregarProducto

urlpatterns = [
    path('v1/', TodosLosProductos.as_view()),
    path('v1/agregarProducto/', AgregarProducto.as_view()),
    path('v1/<int:id_producto>/', ProductoPorId.as_view())
]