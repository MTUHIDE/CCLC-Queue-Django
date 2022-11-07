from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class CanvasCourse(models.Model):
    name = models.TextField()


class Assignment(models.Model):
    course = models.ForeignKey(CanvasCourse, on_delete=models.CASCADE)
    name = models.TextField()


class EnrolledIn(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(CanvasCourse, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Enrollment"
        verbose_name_plural = "Enrollments"
        unique_together = (("user", "course"),)


class Question(models.Model):
    course = models.ForeignKey(CanvasCourse, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    in_person = models.BooleanField(default=False)
    asked_by = models.ForeignKey(User, on_delete=models.CASCADE)
    hidden = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_at"]


class QueueQuestion(Question):
    answered_by = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True
    )


class Reply(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    replied_by = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Replies"


class SupportedCourse(models.Model):
    course_code = models.CharField(max_length=6, primary_key=True)
