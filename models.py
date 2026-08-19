from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    title = models.CharField(max_length=200)

    description = models.TextField()

    due_date = models.DateField()

    status = models.CharField(
        max_length=20,
        default="Pending"
    )

    def __str__(self):
        return self.title