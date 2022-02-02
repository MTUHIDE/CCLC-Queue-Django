from canvasapi import Canvas
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    @property
    def canvas(self):
        canvas_user = self.social_auth.get(provider="canvas-oauth2")
        canvas_url = f"https://{settings.SOCIAL_AUTH_CANVAS_OAUTH2_BASE_URL}"
        return Canvas(canvas_url, canvas_user.extra_data["access_token"])


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
        unique_together = (("user", "course"),)


class Question(models.Model):
    course = models.ForeignKey(CanvasCourse, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    in_person = models.BooleanField(default=False)
    asked_by = models.ForeignKey(User, on_delete=models.CASCADE)


class Reply(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    replied_by = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.BooleanField(default=False)


class SupportedCourse(models.Model):
    course_code = models.CharField(max_length=6, primary_key=True)


admin.site.register(SupportedCourse)
