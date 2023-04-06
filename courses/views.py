from django.shortcuts import render
from . models import Courses

def course_list(request):
    courses = Courses.objects.all().order_by('-date')
    context = {
        'courses': courses
    }
    return render(request, 'courses.html', context)
