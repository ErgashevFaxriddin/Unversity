from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
	path('admin/', admin.site.urls, name='first'),
	path('', views.first_view),
	path('teachers/', views.first_view),
	path('students/', views.first_view)
]