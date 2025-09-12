from django.db import models
from django.contrib.auth import get_user_model
import uuid
from django.utils.text import slugify
from django.core.validators import MinValueValidator,MaxValueValidator

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=200,unique=True)
    description = models.TextField(blank=True,null=True)
    slug = models.SlugField(unique=True,blank=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    class Meta:
        verbose_name_plural = 'Categories'

    def save(self,*args,**kwargs):
        if not self.slug:   #Auto generated if black
            base_slug = slugify(self.name)
            slug = base_slug
            num = 1
            while Category.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{num}"
                num += 1
            self.slug = slug
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True,null=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True,blank=True)
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False,unique=True)

    def save(self,*args,**kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug=base_slug
            num=1
            while Product.objects.filter(slug=slug).exists():
                slug = f'{base_slug}-{num}'
                num+=1
            self.slug = slug
        super().save(*args,**kwargs)
    
    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='images')
    image = models.ImageField(upload_to='media/')
    alt_text = models.CharField(max_length=300,blank=True,null=True)
    is_feature = models.BooleanField(default=False)
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False,unique=True)

    def __str__(self):
        return f'Image for {self.product.name}'
    
class Review(models.Model):
    product = models.ForeignKey(Product,related_name='reviews',on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='reviews',on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1),MaxValueValidator(5)],
        default=1
    )
    comment = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True,editable=False)

    class Meta:
        unique_together = ('product','user')  # prevent duplicate reviews

    def __str__(self):
        return f'{self.user}-{self.product}-({self.rating})'