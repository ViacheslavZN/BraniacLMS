from django.contrib import admin

from .models import News, Courses, CourseTeachers, Lesson

admin.site.register(News)
admin.site.register(Courses)
admin.site.register(CourseTeachers)
admin.site.register(Lesson)