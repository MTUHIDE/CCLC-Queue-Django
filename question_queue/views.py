from datetime import date
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def index(response):
    template = loader.get_template("question_queue/index.html")
    context = {"question_queue": ""}
    return HttpResponse(template.render(context, response))


def student(response):
    template = loader.get_template("question_queue/student/student.html")
    context = {"question_queue": ""}
    return HttpResponse(template.render(context, response))


def instructor(response):
    template = loader.get_template("question_queue/instructor.html")
    context = {"question_queue": ""}
    return HttpResponse(template.render(context, response))


def coach(response):
    template = loader.get_template('question_queue/coach.html')
    context = {'question_queue': ''}
    return HttpResponse(template.render(context, response))
