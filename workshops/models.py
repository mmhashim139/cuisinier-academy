from django.db import models
from datetime import datetime
from experts.models import Expert


class Workshop(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    expert = models.ForeignKey(Expert, on_delete=models.DO_NOTHING)
    main_img = models.ImageField(null=True, blank=True) # upload file path 
    image_1 = models.ImageField(null=True, blank=True)
    image_2 = models.ImageField(null=True, blank=True)
    image_3 = models.ImageField(null=True, blank=True)
    agenda_day_1 = models.TextField(null=True, blank=True)
    agenda_day_2 = models.TextField(null=True, blank=True)
    agenda_day_3 = models.TextField(null=True, blank=True)
    price = models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    location = models.CharField(null=True, max_length=200)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
