from django.shortcuts import render
from .models import Category,Product,ProductImage,Review
from .serializers import CategorySerializer,ProductSerializer,ProductImageSerialzer,ReviewSerializer
from rest_framework import viewsets
from drf_spectacular.utils import extend_schema

@extend_schema(
    tags=['Product-Category']
)
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

@extend_schema(
    tags=['Product-product'],
    description='Product details'
)
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

@extend_schema(
    tags=['Product-Image'],
    description='Image upload here!!!'
)
class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerialzer

@extend_schema(
    tags=['Product-Review'],
    description='Review give here!!!!!'
)
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
