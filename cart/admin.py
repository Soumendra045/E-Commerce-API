from django.contrib import admin
from .models import Cart,CartItem

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user','created_at')
    search_fields = ('user__username','user__email')

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart','product')
    search_fields = ('cart_user__username','product__name')
