from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def student_view(respnse):
    return HttpResponse("You are at the student page!")


@login_required()
def instructor_view(respnse):
    return HttpResponse("You are at the instructor page!")
