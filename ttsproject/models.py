from django.contrib.postgres.fields import JSONField
from django.db import models
from django.conf import settings
from django.utils import timezone 
# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200)
    settings = JSONField()

class Paragraphs(models.Model):
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE
    )
    text = models.TextField()
    audio = models.FileField()
    order = models.IntegerField()