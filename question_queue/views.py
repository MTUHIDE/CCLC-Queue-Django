from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from django.template import loader


# Create your views here.
@login_required
def index(response):
    template = loader.get_template("question_queue/index.html")
    context = {"question_queue": ""}
    return HttpResponse(template.render(context, response))


@login_required
@permission_required("question_queue.can_access_student_view")
def student(response):
    template = loader.get_template("question_queue/student.html")
    context = {"question_queue": ""}
    return HttpResponse(template.render(context, response))


@login_required
@permission_required("question_queue.can_access_instructor_view")
def instructor(response):
    template = loader.get_template("question_queue/instructor.html")
    context = {"question_queue": ""}
    return HttpResponse(template.render(context, response))


@login_required
@permission_required("question_queue.can_access_coach_view")
def coach(response):
    template = loader.get_template("question_queue/coach.html")
    context = {"question_queue": ""}
    return HttpResponse(template.render(context, response))
