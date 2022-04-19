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

    user = "Dr.Professor"

    table_data = [{
        "id": "1",
        "name": "Mark",
        "class": "CS1121",
        "time": "12:30",
        "message": "Question One",
    },
    {
        "id": "2",
        "name": "Johnson",
        "class": "CS1142",
        "time": "12:55",
        "message": "Question Two",
    },
    {
        "id": "3",
        "name": "Larry",
        "class": "CS1121",
        "time": "02:20",
        "message": "Question Three",
    },
    {
        "id": "4",
        "name": "Susan",
        "class": "CS1142",
        "time": "02:55",
        "message": "Question Four",
    }]

    context = {"question_queue": "", "questions": table_data, "user": user}
    return HttpResponse(template.render(context, response))


def coach(response):
    template = loader.get_template("question_queue/coach.html")
    context = {"question_queue": ""}
    return HttpResponse(template.render(context, response))
