import graphene
from graphene_django import DjangoObjectType
from .models import Order

class OrderType(DjangoObjectType):
    class Meta:
        model = Order
        fields = ('id','user','total_price')

class Query(graphene.ObjectType):
    all_orders = graphene.List(OrderType)

    def reslove_all_order(root,info):
        return Order.objects.all()