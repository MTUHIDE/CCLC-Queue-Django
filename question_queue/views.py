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

    test_data = [{
        "id": "1",
        "message": "Question One",
    },
    {
        "id": "2",
        "message": "Question Two",
    },
    {
        "id": "3",
        "message": "Question Three",
    },
    {
        "id": "4",
        "message": "Question Four",
    }]

    context = {"question_queue": "", "questions": test_data}
    return HttpResponse(template.render(context, response))


def question(response):
    template = loader.get_template("question_queue/question.html")
    context = {"question_queue": ""}
    return HttpResponse(template.render(context, response))


def coach(response):
    template = loader.get_template("question_queue/coach.html")
    context = {"question_queue": ""}
    return HttpResponse(template.render(context, response))
