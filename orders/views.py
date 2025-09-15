from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Order
from .serializers import OrderSerializer
from drf_spectacular.utils import extend_schema

@extend_schema(
    tags=['orders'],
    description='Create and update, View order'
)
class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    

    def get_queryset(self):
        # users only see their own orders
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
