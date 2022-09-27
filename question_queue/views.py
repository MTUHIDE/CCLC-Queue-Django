from xmlrpc.client import DateTime
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect

from .models import Question, Reply, User

from .forms import AnswerForm


# Create your views here.
def index(response):
    template = loader.get_template("question_queue/index.html")
    context = {"question_queue": ""}
    return HttpResponse(template.render(context, response))


def student(response):
    template = loader.get_template("question_queue/student/student.html")
    context = {"question_queue": ""}
    return HttpResponse(template.render(context, response))


def getAnswerForm(request):
    form = AnswerForm(request.POST)
    print(form)
    return render(request, "question_queue/instructor.html", {"form": form})


def instructor(request):

    user = User.objects.get(first_name="Jon", last_name="Doe")

    # Query all questions
    questions = Question.objects.all()

    # Initialize data to be
    table_data = []

    # Add all query'd data the table that will passed as context
    for question in questions:
        question_info = {
            "id": str(question.id),
            "name": question.asked_by.first_name,
            "class": question.course.name,
            "time": question.created_at,
            "message": question.message,
        }
        table_data.append(question_info)

    context = {
        "question_queue": "",
        "questions": table_data,
        "user": user,
        "form": AnswerForm,
    }

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            print(cleaned_data)

            question_replied = Question.objects.get(id=request.POST.get("question"))

            # Implement last_updated time if we add an edit reply feature
            reply = Reply(
                question=question_replied,
                message=cleaned_data["message"],
                created_at=DateTime,
                last_updated=DateTime,
                replied_by=user,
                answer=cleaned_data["answer"],
            )
            reply.save()

        # This return makes it so we don't get new POSTs on refresh
        return redirect("/instructor/", context)

    return render(request, "question_queue/instructor.html", context)


def coach(response):
    template = loader.get_template("question_queue/coach.html")
    context = {"question_queue": ""}
    return HttpResponse(template.render(context, response))
