import factory
from factory.django import DjangoModelFactory
from question_queue.models import (
    User,
    Question,
    CanvasCourse,
    Assignment,
    Reply,
    QueueQuestion,
)


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ("username",)

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


class AssignmentFactory(DjangoModelFactory):
    class Meta:
        model = Assignment

    name = factory.Faker(
        "random_element",
        elements=(
            "Easy Programming Homework",
            "Advanced Programming Homework",
            "Extra Advanced Programming Homework",
        ),
    )

    course = factory.SubFactory(CanvasCourseFactory)


class QuestionFactory(DjangoModelFactory):
    class Meta:
        model = Question

    course = factory.SubFactory(CanvasCourseFactory)
    assignment = factory.SubFactory(AssignmentFactory)
    asked_by = factory.SubFactory(UserFactory)
    message = factory.Faker(
        "random_element",
        elements=(
            "What is a variable?",
            "How do I create a class?",
            "I need help with a question on my homework!",
        ),
    )
    created_at = factory.Faker("date")
    last_updated = factory.Faker("date")
    hidden = factory.Faker("boolean")


class ReplyFactory(DjangoModelFactory):
    class Meta:
        model = Reply

    question = factory.SubFactory(QuestionFactory)
    replied_by = factory.SubFactory(UserFactory)

    message = factory.Faker(
        "random_element",
        elements=(
            "Let me help you with that!",
            "I'm not sure...",
            "This is the answer!",
        ),
    )

    created_at = factory.Faker("date")
    last_updated = factory.Faker("date")
    answer = factory.Faker("boolean")


class QueueQuestionFactory(QuestionFactory):
    class Meta:
        model = QueueQuestion

    answered_by = factory.SubFactory(UserFactory)
