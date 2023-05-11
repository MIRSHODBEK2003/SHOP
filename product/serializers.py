from rest_framework.serializers import ModelSerializer
from .models import Category,Product


class ChildCategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"

class CategorySerializer(ModelSerializer):
    child_category_obj = ChildCategorySerializer(source="category_set", many=True, read_only=True)

    class Meta:
        model = Category
        fields = "__all__"

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"