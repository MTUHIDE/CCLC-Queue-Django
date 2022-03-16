from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class CanvasCourse(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()


class Assignment(models.Model):
    id = models.IntegerField(primary_key=True)
    course = models.ForeignKey(CanvasCourse, on_delete=models.CASCADE)
    name = models.TextField()


class EnrolledIn(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(CanvasCourse, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("user_id", "course_id"),)


class Question(models.Model):
    course = models.ForeignKey(CanvasCourse, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField()
    last_updated = models.DateTimeField()
    in_person = models.BooleanField()
    asked_by = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.ForeignKey(
        "Reply", blank=True, null=True, default=None, on_delete=models.CASCADE
    )  # Reply is a string as it is not defined yet


class Reply(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField()
    last_updated = models.DateTimeField()
    replied_by = models.ForeignKey(User, on_delete=models.CASCADE)


class SupportedCourse(models.Model):
    course_code = models.CharField(6, primary_key=True)
