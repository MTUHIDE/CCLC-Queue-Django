from datetime import date
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .forms import QuestionForm


# Create your views here.
def index(response):
    template = loader.get_template('question_queue/index.html')
    context = {'question_queue': ''}
    if response.GET:
        temp = response.GET['geeks_field']
        print(temp)
    return HttpResponse(template.render(context, response))


def student(response):
    template = loader.get_template('question_queue/student/student.html')
    # context = {'question_queue': '', "hello": "world"}
    context = {'question_queue': '', "hello": "world",
               "openQuestions": {"1": {"id": "123"}, "2": {"id": 123}}, 'form': QuestionForm()}
    return HttpResponse(template.render(context, response))


def instructor(response):
    template = loader.get_template('question_queue/instructor.html')
    context = {'question_queue': ''}
    return HttpResponse(template.render(context, response))

def coach(response):
    template = loader.get_template('question_queue/coach.html')
    context = {'question_queue': ''}
    return HttpResponse(template.render(context, response))
