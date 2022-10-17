from django.db import transaction
from django.core.management.base import BaseCommand
from question_queue.models import User, CanvasCourse


@transaction.atomic
class Command(BaseCommand):
    help = "Deletes dummy data from our app"

    def handle(self, *args, **kwargs):
        print("Deleting Users...\n")

        user_list = User.objects.all().exclude(is_superuser=True)
        course_list = CanvasCourse.objects.all()

        for m in user_list:
            print(m)
            m.delete()

        for c in course_list:
            print(c)
            c.delete()
