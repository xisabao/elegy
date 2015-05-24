from django.contrib import admin
from .models import TheClass, Post, Assignment
# Register your models here.
admin.site.register(TheClass)
admin.site.register(Assignment)
admin.site.register(Post)