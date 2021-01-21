from django.db import models


# Create your models here.
class Expert(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField(blank=True)
    profile_image = models.ImageField(null=True, blank=True)
    facbook_link = models.CharField(default='www.facebook.com', max_length=200)
    twitter_link = models.CharField(default='www.twitter.com', max_length=200)
    # classes ?

    def __str__(self):
        return self.name
