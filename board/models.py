from django.db import models

# Create your models here.

class JobOffer(models.Model):
    title = models.CharField(max_length = 100)
    short_description = models.CharField(max_length = 300, blank = True)
    lower_rate = models.FloatField(blank=True)
    upper_rate = models.FloatField(blank=True)
    description = models.CharField(max_length = 5000)