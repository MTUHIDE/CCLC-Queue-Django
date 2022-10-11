import factory
from factory.django import DjangoModelFactory
from question_queue.models import User


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    username = factory.LazyAttribute(lambda a: f"{a.first_name}.{a.last_name}".lower())
