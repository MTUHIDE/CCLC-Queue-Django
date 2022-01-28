from django.urls import path
from . import views

urlpatterns = [
    path("student/", views.student_view, name="student view"),
    path("instructor/", views.instructor_view, name="instructor view"),
]
