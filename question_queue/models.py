from django.db import models


class Question(models.Model):
    user_name = models.CharField(
        max_length=32
    )  # Should be max 6 chars, but lets play it safe
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField()
    password = models.CharField(max_length=256)
    groups = models.CharField(max_length=256)


class Answer(models.Model):
    question_id = models.ForeignKey(
        Question, on_delete=models.CASCADE
    )  # Might need to change this
    message = models.CharField(max_length=256)
    created_at = models.DateTimeField()
    last_updated = models.DateTimeField()
