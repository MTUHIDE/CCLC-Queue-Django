from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # default path
    path("student/", views.student, name="student view"),
    path("instructor/", views.instructor, name="instructor view"),
    path("question/", views.question, name="question view"),
    path("coach/", views.coach, name="coach view"),
]
