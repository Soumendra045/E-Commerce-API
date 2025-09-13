from django.db import models
from django.conf import settings
from products.models import Product
import uuid

class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='cart')
    created_at =models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True,editable=False)

    def __str__(self):
        return f'Cart of {self.user.username}'
    
    @property
    def total_Item(self):
        return sum(item.subtotal for item in self.items.all())
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='items')
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True,editable=False)

    class Meta:
        unique_together = ('cart','product')

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'
    
    @property
    def subtotal(self):
        return self.product.price * self.quantity