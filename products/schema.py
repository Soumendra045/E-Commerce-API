import graphene
from graphene_django import DjangoObjectType
from .models import Product,Category

class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = ("id", "name", "price", "is_active","created_at")

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id","name")

class Query(graphene.ObjectType):
    all_products = graphene.List(ProductType)
    all_category = graphene.List(CategoryType)

    def reslove_all_product(root,info):
        return Product.objects.all()
    
    def reslove_all_category(root,info):
        return Category.objects.all()