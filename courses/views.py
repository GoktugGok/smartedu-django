from django.shortcuts import render
from . models import Courses, Category, Tag
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

def course_detail(request, category_slug, course_id):
    course = Courses.objects.get(category__slug=category_slug,id= course_id)
    user = request.user
    notagain = course.students.all().filter(id = user.id)
    context = {
        'course': course,
        'user' : user,
        'notagain': notagain,
    }

    return render(request,'course.html',context)

def course_list(request, category_slug=None,tag_slug=None):
    category_page = None
    tag_page = None
    categories = Category.objects.all()
    tags = Tag.objects.all()

    if category_slug != None:
        category_page = get_object_or_404(Category, slug=category_slug)
        courses = Courses.objects.filter(available=True,category=category_page)

    elif tag_slug != None:
        tag_page = get_object_or_404(Tag, slug=tag_slug)
        courses = Courses.objects.filter(available=True, tags=tag_page)

    else:
        courses = Courses.objects.all().order_by("-date")

    context = {
        'courses': courses,
        'categories': categories,
        'tags': tags
    }
    return render(request, 'courses.html', context)

def search(request):
    courses = Courses.objects.all().filter(name__contains = request.GET['search'])
    categories = Category.objects.all()
    tags = Tag.objects.all()

    context = {
        'courses': courses,
        'categories': categories,
        'tags': tags
    }
    return render(request, 'courses.html', context)


"""def course_list(request):
    courses = Courses.objects.all().order_by('-date')
    categories = Category.objects.all()
    tags = Tag.objects.all()

    context = {
        'courses': courses,
        'categories': categories,
        'tags': tags
    }
    return render(request, 'courses.html', context)"""

"""
def category_list(request, category_slug):
    courses = Courses.objects.all().filter(category__slug = category_slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()

    context = {
        'courses': courses,
        'categories': categories,
        'tags': tags
    }

    return render(request,'courses.html',context)

def tag_list(request, tag_slug):
    courses = Courses.objects.all().filter(tags__slug = tag_slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()

    context = {
        'courses': courses,
        'categories': categories,
        'tags': tags
    }

    return render(request,'courses.html',context)
"""
