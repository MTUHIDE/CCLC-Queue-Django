from django.http import HttpResponse

# Create your views here.


def student_view(respnse):
    return HttpResponse("You are at the student page!")


def instructor_view(respnse):
    return HttpResponse("You are at the instructor page!")
