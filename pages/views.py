from django.shortcuts import render
from django.views.generic import TemplateView
from courses.models import Courses


# from django.views.generic import TemplateView
# from courses.models import Courses

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Courses.objects.filter(available=True).order_by("-date")[:2]
        return context

class AboutView(TemplateView):
    template_name = 'about.html'

# class IndexView(TemplateView):
#     template_name = 'index.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['courses'] = Courses.objects.filter(available=True).order_by("-date")[:2]
#         context['total_course'] = Courses.objects.filter(available=True).count()
#         return context

# def home(request):
#      return render(request, 'index.html')

# class AboutView(TemplateView):
#     template_name = 'about.html'

# def about(request):
#     return render(request, 'about.html')

# Create your views here.
