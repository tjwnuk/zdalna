from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300, null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

class JobOffer(models.Model):
    title = models.CharField(max_length = 100)
    short_description = models.CharField(max_length = 300, blank = True)
    lower_rate = models.FloatField(blank=True)
    upper_rate = models.FloatField(blank=True)
    description = models.CharField(max_length = 5000)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ' : ' + self.company.name
