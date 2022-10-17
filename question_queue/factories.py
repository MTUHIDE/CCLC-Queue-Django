import factory
from factory.django import DjangoModelFactory
from question_queue.models import User, Question, CanvasCourse


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    username = factory.LazyAttribute(lambda a: f"{a.first_name}{a.last_name}".lower())


class CanvasCourseFactory(DjangoModelFactory):
    class Meta:
        model = CanvasCourse

    name = factory.Faker(
        "random_element",
        elements=(
            "Intro To Programming",
            "Advanced Programming",
            "Extra Advanced Programming",
        ),
    )


class QuestionFactory(DjangoModelFactory):
    class Meta:
        model = Question
