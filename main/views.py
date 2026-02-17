from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first_view(request):
    html = f"""
    
    <h1>Tashkent Information Technology University Fergana Branch</h1>
    <a href="/teachers/"/> TEACHERS >> </a><br>
    <a href="/students/"> STUDENTS >> </a><br>
    <a href="/students/"> FACULTY >> </a><br>
    <a href="/students/"> COURSES >> </a><br>
    <a href="/students/"> FINANCE >> </a><br>
    <a href="/students/"> RESOURCE >> </a><br>
    <a href="/students/"> REPORTS >> </a><br>
    <!--<a href="/"> FIRST PAGE << </a> this is a comment -->
    """

    return HttpResponse(html)


def pages(request, page):
    if page == 'teachers':
        html = f"""
        
        <h1>{page}</h1>
        <p>
        A teacher, also called a schoolteacher or formally an educator, is a person who helps students to acquire knowledge, competence, or virtue, via the practice of teaching.
        Informally the role of teacher may be taken on by anyone (e.g. when showing a colleague how to perform a specific task). In some countries, teaching young people of school age may be carried out in an informal setting, such as within the family (homeschooling), rather than in a formal setting such as a school or college. Some other professions may involve a significant amount of teaching (e.g. youth worker, pastor).
        </p>
        <a href="/"> << FIRST PAGE </a>
        """
    elif page == 'students':
        html = f"""

        <h1>{page}</h1>
        <p>
        A student is a person enrolled in a school or other educational institution, or more generally, a person who takes a special interest in a subject.[1]
        In the United Kingdom and most commonwealth countries, a "student" attends a secondary school or higher (e.g., college or university); those in primary or elementary schools are "pupils".[2]
        </p>
        <a href="/"> << FIRST PAGE </a>
        """

    else:
        html = '<h1>PAGE NOT FOUND</h1><a href="/"> << FIRST PAGE</a>'

    return HttpResponse(html)