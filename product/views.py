from .serializers import ProductSerializer, CategorySerializer
from .models import Category, Product
from rest_framework.viewsets import ModelViewSet


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewset(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


