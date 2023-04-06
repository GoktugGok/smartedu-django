from django.contrib import admin
from . models import Courses

@admin.register(Courses)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name','available')
    list_filter = ('available',)
    search_fields = ('name', 'description')

# Register your models here.
