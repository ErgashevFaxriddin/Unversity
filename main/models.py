from django.db import models
from django.utils.text import slugify
# Create your models here.

class Students(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    age = models.SmallIntegerField(blank=True, null=True)
    link = models.URLField(null=True)

