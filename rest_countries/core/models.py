from django.db import models

# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=50, unique=True)

class Language(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=100)

    


class Country(models.Model):
    name = models.CharField(max_length=100)
    cca2 = models.CharField(max_length=2)
    capital = models.CharField(max_length=100, blank=True, null=True)
    population = models.IntegerField()
    timezones = models.JSONField()
    flag_url = models.URLField()
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, related_name='countries')
    languages = models.ManyToManyField(Language, related_name='countries')
