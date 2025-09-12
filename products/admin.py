from django.contrib import admin
from .models import Category,Product,ProductImage,Review

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug')  #show coloum 
    search_fields = ('name',)     # add a search bar 
    prepopulated_fields = {'slug':('name',)}   # auto generated slog in admin

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'is_active')
    list_filter = ('category', 'is_active')   # add sidebar filter
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)} # auto slug from name
    ordering = ('-created_at',)


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'is_feature')
    list_filter = ('is_feature',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('comment',)
