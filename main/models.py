from django.utils import timezone
from django.db import models
from django.forms import CharField
from django.utils.text import slugify
# Create your models here.

class Students(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    age = models.SmallIntegerField(blank=True, null=True)
    link = models.URLField(null=True)

    def __str__(self):
        return self.name.title()


class Faculty(models.Model):
    professor = models.CharField(max_length=100)
    assigned_course = models.CharField(max_length=100)

    def __str__(self):
        return self.professor.title()


class Teachers(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # degree = models.CharField(max_length=100, blank=True, null=True)
    # email = models.CharField(max_length=150)
    phone_number = models.SmallIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name.title()


class Subjects(models.Model):
    name = models.CharField(max_length=100)
    credit = models.SmallIntegerField(max_length=150)
    resources = models.SmallIntegerField(max_length=10)
    tasks_number = models.SmallIntegerField(max_length=10)

    def __str__(self):
        return self.name.title()


class Finance(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    condition = models.CharField(max_length=50)
    course = models.SmallIntegerField()
    major = models.CharField(max_length=150)
    students = models.ForeignKey(Students, null=True, on_delete=models.CASCADE)
