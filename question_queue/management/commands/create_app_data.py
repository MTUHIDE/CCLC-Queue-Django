from django.db import transaction
from django.core.management.base import BaseCommand
from question_queue.factories import ReplyFactory, QueueQuestionFactory


@transaction.atomic
class Command(BaseCommand):
    help = "Create's dummy data for the question queue app"

    def handle(self, *args, **kwargs):
        print("Creating Dummy Data...\n")
        for _ in range(100):
            ReplyFactory()
            QueueQuestionFactory()
