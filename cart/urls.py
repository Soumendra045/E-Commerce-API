from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import CartViewSet,CartItemViewset

router = DefaultRouter()

router.register('cart',CartViewSet,basename='cart')
router.register('cartitem',CartItemViewset,basename='cartitem')

urlpatterns = [
    path('',include(router.urls)),
]
