from django.db import models


# Task Model

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    date = models.DateField()

    def __str__(self):
        return self.title
