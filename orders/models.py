from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product
import uuid

User=get_user_model()

class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PROCESSING', 'Processing'),
        ('SHIPPED', 'Shipped'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    total_price = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    def update_total(self):
        self.total_price = sum(item.price * item.quantity for item in self.items.all())
        super().save(update_fields=['total_price'])  # only update total_price

    def __str__(self):
        return f'Order {self.id} by {self.user.username} - {self.status}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.price:  # if empty, copy from product
            self.price = self.product.price
        super().save(*args, **kwargs)
        # update order total after saving this item
        self.order.update_total()

    def __str__(self):
        return f'{self.quantity} x {self.product.name} (Order {self.order.id})'

