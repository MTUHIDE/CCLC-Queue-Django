from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render


# Create your views here.
def index(response):
    template = loader.get_template('question_queue/index.html')
    context = {'question_queue': ''}
    return HttpResponse(template.render(context, response))


def student(response):
    template = loader.get_template('question_queue/student.html')
    context = {'question_queue': ''}
    return HttpResponse(template.render(context, response))


def instructor(response):
    template = loader.get_template('question_queue/instructor.html')
    context = {'question_queue': ''}
    return HttpResponse(template.render(context, response))

def coach(response):
    template = loader.get_template('question_queue/coach.html')
    context = {'question_queue': ''}
    return HttpResponse(template.render(context, response))
