from django.shortcuts import render
from .models import Cart,CartItem
from .serializers import CartSerializer,CartItemSerializer
from rest_framework import viewsets

class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
class CartItemViewset(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer

    def get_queryset(self):
        return CartItem.objects.filter(cart__user=self.request.user)
    
    def perform_create(self, serializer):
        cart,created = Cart.objects.get_or_create(user=self.request.user)
        serializer.save(cart=cart)