from django.urls import path
from . import views

urlpatterns = [
	path('', views.first_view, name='first'),
	path('<str:page>/', views.pages, name='pages'),

]