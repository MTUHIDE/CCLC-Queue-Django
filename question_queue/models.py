from django.db import models


class Question(models.Model):
    id = models.BigIntegerField() # PRIMARY KEY
    user_name = models.CharField(max_length=32) # Should be max 6 chars, but lets play it safe
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField()
    password = models.CharField(max_length=256)
    groups = models.CharField(max_length=256)