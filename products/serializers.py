from rest_framework import serializers
from .models import Category,Product,ProductImage,Review

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        depth = 1

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        depth = 1

class ProductImageSerialzer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'
        depth = 1

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        depth = 1