from django.db import models
from datetime import datetime, date
# Create your models here.
# class Task(models.Model):
#     title = models.CharField(max_length=200)
#     complete = models.BooleanField(default=False)
#     created = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.title


class Task(models.Model):
    """A project the user is working on."""
    text = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text


class TaskWork(models.Model):
    """A task of a project to complete."""
    project = models.ForeignKey(Task, on_delete=models.CASCADE)
    taskleft = models.CharField(max_length=400)
    date_added = models.DateField("Expected Task Completion Date(mm/dd/yyyy)",auto_now_add=False, auto_now=False, blank=True)
    # datecomp = models.CharField(max_length=400)

    class Meta:
        verbose_name_plural = 'taskswork'

    def __str__(self):
        """Return a string representation of the model."""
        # if(len(self.project) < 50 ):
        return self.taskleft+ " " + str(self.date_added)
        # else:
        #     return f"{self.project[:50]}..."
