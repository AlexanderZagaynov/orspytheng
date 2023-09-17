import graphene
from graphene_django import DjangoObjectType

from cars.models import Car

class CarType(DjangoObjectType):
    class Meta:
        model = Car
        fields = ("uid", "make", "model")

class Query(graphene.ObjectType):
    all_cars = graphene.List(CarType)

    def resolve_all_cars(root, info):
        return Car.objects.all()

schema = graphene.Schema(query=Query)
