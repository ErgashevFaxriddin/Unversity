from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first_view(request):
    html = f"""
    
    <h1>Tashkent Information Technology University Fergana Branch</h1>
    <a href="/teachers"> TEACHERS >> </a><br>
    <a href="/students"> STUDENTS >> </a>
    <a href=/first_page"> FIRST PAGE << </a>
    
    """
    return HttpResponse(html)