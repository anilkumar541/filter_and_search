from django.shortcuts import render

from rest_framework.generics import ListAPIView
from app.models import Category, Product
from app.serializers import CategorySerializer, ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.filters import SearchFilter

class CategoryListView(ListAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    # sort based on created_at(asc and desc)
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['category_name'] # filter by category_name=mobile
    ordering_fields=["created_at"] #order by created_at
 


class ProductListView(ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    print(serializer_class)

    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['product_name', "category"]
    ordering_fields=["created_at"]
    search_fields = ["product_name", "category__category_name"]

  

