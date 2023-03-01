from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=64)
    time = models.CharField(blank=True,max_length=10)
