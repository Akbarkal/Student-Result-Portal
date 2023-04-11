from django.contrib import admin
from django.contrib.auth.models import Group
from .models import faculty_login,students

# Register your models here.

# class studentsAdmin(admin.ModelAdmin):
#     list_display = ('students')


admin.site.register(faculty_login)
admin.site.register(students)
# admin.site.unregister(Group)