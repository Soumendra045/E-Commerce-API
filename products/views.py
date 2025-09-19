from django.shortcuts import render
from .models import Category,Product,ProductImage,Review
from .serializers import CategorySerializer,ProductSerializer,ProductImageSerialzer,ReviewSerializer
from rest_framework import viewsets
from drf_spectacular.utils import extend_schema,OpenApiParameter,OpenApiTypes
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import filters
from django.db.models import Q


@extend_schema(
    tags=['Product-Category']
)
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


@extend_schema(
    tags=['Product-product'],
    description='Product details',

    parameters=[
        OpenApiParameter("search", OpenApiTypes.STR, OpenApiParameter.QUERY, description="Search term"),
        OpenApiParameter("min_price", OpenApiTypes.NUMBER, OpenApiParameter.QUERY, description="Minimum price"),
        OpenApiParameter("max_price", OpenApiTypes.NUMBER, OpenApiParameter.QUERY, description="Maximum price"),
        OpenApiParameter("category", OpenApiTypes.STR, OpenApiParameter.QUERY, description="Category name"),
    ]
    

)
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_class = ProductFilter

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
