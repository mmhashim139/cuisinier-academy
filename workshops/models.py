from django.db import models


class Workshop(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
