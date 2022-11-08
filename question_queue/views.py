from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect

from .models import Question, QueueQuestion

from .forms import QuestionForm, AnswerForm, FilterQueue


def index(response):
    template = loader.get_template("question_queue/index.html")
    context = {"question_queue": ""}
    return HttpResponse(template.render(context, response))


def student(request):
    user = "Little Student"
    context = {
        "user": user,
        "form": QuestionForm,
    }

    if request.method == "POST":
        print(request.POST.get("course", "error"))
        print(request.POST.get("asked_by", user))
        print(request.POST.get("question", "error"))
        print(request.POST.get("in_person", "off"))
        # This return makes it so we don't get new POSTs on refresh
        return redirect("/student", context)

    return render(request, "question_queue/student/student.html", context)


def instructor(request):
    user = "Dr.Professor"
    table_data = grabQuestions()

    context = {
        "questions": table_data,
        "user": user,
        "form": AnswerForm,
    }

    if request.method == "POST":
        print(request.POST.get("question", "error"))
        print(request.POST.get("replied_by", user))
        print(request.POST.get("message", "error"))
        print(request.POST.get("answer", "off"))
        # This return makes it so we don't get new POSTs on refresh
        return redirect("/instructor/", context)

    return render(request, "question_queue/instructor.html", context)


def coach(request):
    user = "dannyshannon"
    table_data = grabQuestions()

    context = {
        "questions": table_data,
        "user": user,
        "form": AnswerForm,
        "filter": "",
    }

    if request.method == "POST":
        if "filter_queue" in request.POST:
            queueFilter = FilterQueue(request.POST)
            if queueFilter.is_valid():
                queueFilterMode = request.POST.get("filter_queue", "error")
                context["questions"] = filterHelper(table_data, queueFilterMode)
            else:
                # Do something if request is dropped
                pass
            return render(request, "question_queue/coach.html", context)
        print(request.POST.get("question", "error"))
        print(request.POST.get("replied_by", user))
        print(request.POST.get("message", "error"))
        print(request.POST.get("answer", "off"))
        # This return makes it so we don't get new POSTs on refresh
        return redirect("/coach/", context)

    return render(request, "question_queue/coach.html", context)


def forum(request):
    if request.method == "GET":
        user = "Little Student"
        table_data = grabQuestions()

        context = {
            "questions": table_data,
            "user": user,
            "filter": None,
        }
        return render(request, "question_queue/forum/forum.html", context)
    elif request.method == "POST":
        return render(request, "question_queue/forum/forum.html", context)


def forumQuestion(request, question_id=None):
    if request.method == "GET":
        user = "Little Student"
        table_data = grabQuestions()
        question_details = None
        for q in table_data:
            print(q["id"])
            if q["id"] == str(question_id):
                question_details = q
                break
        if question_details is None:
            return HttpResponse("<p style='color:red'>ERROR: Bad question ID</p>")

        context = {
            "question": question_details,
            "user": user,
            "form": None,
        }
        return render(request, "question_queue/forum/question_detailed.html", context)
    elif request.method == "POST":
        return render(request, "question_queue/forum/question_detailed.html", context)


def filterHelper(questionQueue, mode):
    if mode == "open":
        # All unanswered questions
        return [question for question in questionQueue if not question["answered"]]
    elif mode == "answered":
        # All answered questions
        return [question for question in questionQueue if question["answered"]]
    else:
        # Just the normal queue
        return questionQueue


def grabQuestions():
    questions = Question.objects.all()
    # Initialize data list
    table_data = []
    # Add all query'd data the table that will passed as context
    for question in questions:
        # Should only ever be 1 or 0 because unique IDs
        queueQuestion = QueueQuestion.objects.filter(id=question.id)
        answeredBy = queueQuestion[0].answered_by.username if queueQuestion else None
        question_info = {
            "id": str(question.id),
            "name": question.asked_by.first_name,
            "class": question.course.name,
            "time": question.created_at.time,
            "message": question.message,
            "hidden": question.hidden,
            "answered": answeredBy,
        }
        if not question_info["hidden"]:
            table_data.append(question_info)
    return table_data
