from django.contrib import admin
from . models import Courses ,Category, Tag

@admin.register(Courses)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name','available','teacher',)
    list_filter = ('available',)
    search_fields = ('name', 'description')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug':('name',)}
    
@admin.register(Tag)
class Tag(admin.ModelAdmin):
    prepopulated_fields ={'slug':('name',)}

# Register your models here.
