from django.shortcuts import render
from . models import Courses

def course_list(request):
    courses = Courses.objects.all().order_by('-date')
    context = {
        'courses': courses
    }
    return render(request, 'courses.html', context)

def course_detail(request, category_slug, course_id):
    course = Courses.objects.get(category__slug=category_slug,id= course_id)

    context = {
        'course': course
    }

    return render(request,'course.html',context)
