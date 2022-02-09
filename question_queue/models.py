from django.db import models


class Question(models.Model):
    version = models.BigIntegerField()
    course_name = models.CharField(max_length=256)
    is_deleted = models.BooleanField()
    date_created = models.DateTimeField()
    assignment_date = models.CharField(max_length=256)
    last_updated = models.DateTimeField()
    deleted_by_id = (
        models.BigIntegerField()
    )  # MAKE FOREIGN KEY WHEN USER TABLE IS ADDED
    language = models.CharField(max_length=256)
    message = models.TextField()
    is_answered = models.BooleanField()
    person_id = models.BigIntegerField()  # MAKE FOREIGN KEY WHEN USER TABLE IS ADDED
    ipaddress = models.CharField(max_length=256)
    hostname = models.CharField(max_length=256)
    course = models.CharField(max_length=256)
    is_hand_raised = models.BooleanField()
    assignment = models.CharField(max_length=256)
    subject = models.CharField(max_length=256)
