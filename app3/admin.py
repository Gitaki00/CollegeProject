from django.contrib import admin
from .models import FormData,Course
# Register your models here.
from django.contrib import admin
from .models import Course, FormData

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Course,CourseAdmin)

class FormDataAdmin(admin.ModelAdmin):
    list_display = ['name', 'dob', 'age', 'gender', 'phno', 'email', 'address',  'purpose', 'course']
    list_filter = [ 'course']
    search_fields = ['name', 'email']
admin.site.register(FormData,FormDataAdmin)


