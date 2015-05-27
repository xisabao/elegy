from django.contrib import admin
from .models import TheClass, Post, Assignment, Student, Teacher, StudentToClass, TeacherToClass, Discussion, DiscussionPosts

class StudentToClassInline(admin.TabularInline):
	model = StudentToClass
	extra = 1

class TeacherToClassInline(admin.TabularInline):
	model = TeacherToClass
	extra = 1

class StudentAdmin(admin.ModelAdmin):
	inlines = (StudentToClassInline,)

class TheClassAdmin(admin.ModelAdmin):
	inlines = (StudentToClassInline, TeacherToClassInline)

class TeacherAdmin(admin.ModelAdmin):
	inlines = (TeacherToClassInline,)

# Register your models here.
admin.site.register(TheClass, TheClassAdmin)
admin.site.register(Assignment)
admin.site.register(Post)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Discussion)
admin.site.register(DiscussionPosts)