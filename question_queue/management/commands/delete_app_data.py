from django.db import transaction
from django.core.management.base import BaseCommand
from question_queue.models import User


@transaction.atomic
class Command(BaseCommand):
    help = "Deletes dummy data from our app"

    def handle(self, *args, **kwargs):
        print("Deleting Users...\n")
        user_list = User.objects.all().exclude(username="ADMIN")

        for m in user_list:
            print(m)
            m.delete()
