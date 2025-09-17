import graphene
import products.schema
import orders.schema

class Query(products.schema.Query,orders.schema.Query,graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)