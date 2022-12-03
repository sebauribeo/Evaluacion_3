from django.urls import path, include
from .views import ProductApiView, ProductDetailApiView

urlpatterns = [
    path('v1/', ProductApiView.as_view()),
    path('v1/<int:id_producto>/', ProductDetailApiView.as_view())
]