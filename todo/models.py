from django.db import models

# Create your models here.

class Task(models.Model):
    description = models.CharField(max_length=100)
    due_date = models.DateField()

    def __str__(self):
        return self.description
