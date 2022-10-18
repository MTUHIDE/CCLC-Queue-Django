from django.db import transaction
from django.core.management.base import BaseCommand
from question_queue.models import (
    Assignment,
    Question,
    User,
    CanvasCourse,
    Reply,
    QueueQuestion,
)


@transaction.atomic
class Command(BaseCommand):
    help = "Deletes dummy data from our app"

    def handle(self, *args, **kwargs):
        print("Deleting Fake Data...\n")

        user_list = User.objects.all().exclude(is_superuser=True)
        course_list = CanvasCourse.objects.all()
        assignment_list = Assignment.objects.all()
        question_list = Question.objects.all()
        reply_list = Reply.objects.all()
        queue_question_list = QueueQuestion.objects.all()

        # Deletes ALL dummy data in the app
        for r in reply_list:
            r.delete()

        for q in question_list:
            q.delete()

        for m in user_list:
            m.delete()

        for c in course_list:
            c.delete()

        for a in assignment_list:
            a.delete()

        for z in queue_question_list:
            z.delete()
