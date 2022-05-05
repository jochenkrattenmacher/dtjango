from django.db import models
from django.urls import reverse


class Agent(models.Model):
    name = models.CharField(
        default="",
        unique=True,
        max_length=255,
    )

    def __str__(self):
        return (
            self.name
        )  # self.id + ' email:' + self.email + ' username:' + self.username

    def get_absolute_url(self):
        return reverse("abm:detail", kwargs={"id": self.id})
