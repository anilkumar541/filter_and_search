from rest_framework import serializers
from app.models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id', 'category_name', "created_at", "updated_at"]


class ProductSerializer(serializers.ModelSerializer):
    category=serializers.CharField(read_only=True)
    class Meta:
        model = Product
        fields=['id', "product_name", "category", "created_at", "updated_at"]
        