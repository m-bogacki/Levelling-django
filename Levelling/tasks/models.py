from django.db import models
from enum import Enum

# Create your models here.


class Status(Enum):
    TODO = 1
    IN_PROGRESS = 2
    DONE = 3


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.IntegerField(choices=[(tag.value, tag.name) for tag in Status])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
