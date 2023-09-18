import graphene
from graphene_django import DjangoObjectType

from cars.models import Car


class CarType(DjangoObjectType):
    uid = graphene.String()

    class Meta:
        model = Car
        fields = ("uid", "make", "model")


class CarCreate(graphene.ClientIDMutation):
    car = graphene.Field(CarType)

    class Input:
        uid = graphene.String(required=False, default=None) # autoassign if undefined
        make = graphene.String(required=True)
        model = graphene.String(required=True)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        car_data = {key: input[key] for key in CarType._meta.fields.keys() if key in input}
        car = Car.objects.create(**car_data)
        return cls(car=car)


class CarUpdate(graphene.Mutation):
    car = graphene.Field(CarType)

    class Arguments:
        uid = graphene.ID(required=True)
        make = graphene.String()
        model = graphene.String()

    @classmethod
    def mutate(cls, root, info, **input):
        car_id = Car.uid_to_id(input['uid'])
        car = Car.objects.get(pk=car_id)
        # car_data = {key: input[key] for key in ['make', 'model'] if key in input}
        if 'make' in input:
            car.make = input['make']
        if 'model' in input:
            car.model = input['model']
        car.save()
        return cls(car=car)


class CarDelete(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        uid = graphene.ID(required=True)

    @classmethod
    def mutate(cls, root, info, uid):
        car_id = Car.uid_to_id(uid)
        car = Car.objects.get(pk=car_id)
        car.delete()
        return cls(ok=True)


class Query(graphene.ObjectType):
    all_cars = graphene.List(CarType)

    def resolve_all_cars(root, info):
        return Car.objects.all()


class Mutation(graphene.ObjectType):
    car_create = CarCreate.Field()
    car_update = CarUpdate.Field()
    car_delete = CarDelete.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
