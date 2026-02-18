from django.contrib import admin
from .models import Students, Teachers, Faculty, Subjects, Finance

# Register your models here.
admin.site.register(Students)
admin.site.register(Teachers)
admin.site.register(Faculty)
admin.site.register(Subjects)
admin.site.register(Finance)