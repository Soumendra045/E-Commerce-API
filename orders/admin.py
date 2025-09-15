from django.contrib import admin
from .models import Order,OrderItem

class OrderItemLine(admin.TabularInline):
    model = OrderItem
    extra = 1
    readonly_fields = ('price',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "status", "total_price", "created_at", "updated_at")
    list_filter = ("status", "created_at")
    search_fields = ("user__username","id")
    inlines = [OrderItemLine]

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "product", "quantity", "price")
    list_filter = ("product",)
    search_fields = ("product__name", "order__id")