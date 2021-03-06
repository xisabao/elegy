
# Create your models here.
from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class TheClass(models.Model):

	classname = models.CharField(max_length=200)
	

	def __str__(self):
		return self.classname

class Student(models.Model):
	user = models.OneToOneField(User)
	theclass = models.ManyToManyField(TheClass, through="StudentToClass")
	def __str__(self):
		return self.user.username

class Teacher(models.Model):
	user = models.OneToOneField(User)
	theclass = models.ManyToManyField(TheClass, through="TeacherToClass")

	def __str__(self):
		return self.user.username



class StudentToClass(models.Model):
	student = models.ForeignKey(Student)
	theclass = models.ForeignKey(TheClass)

class TeacherToClass(models.Model):
	teacher = models.ForeignKey(Teacher)
	theclass = models.ForeignKey(TheClass)

class Post(models.Model):
	
	theclass = models.ForeignKey(TheClass)
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default = timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)


	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

class Assignment(models.Model):
	theclass = models.ForeignKey(TheClass)
	title = models.CharField(max_length=200)
	description = models.TextField()
	created_date = models.DateTimeField(default = timezone.now)
	due_date = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return self.title

class Discussion(models.Model):
	title = models.CharField(max_length=200)
	creator = models.ForeignKey('auth.User')
	description = models.TextField()
	theclass = models.ForeignKey(TheClass)
	created_date = models.DateTimeField(default = timezone.now)

	def __str__(self):
		return self.title

class DiscussionPosts(models.Model):
	title = models.CharField(max_length = 200)
	author = models.ForeignKey('auth.User')
	text = models.TextField()
	published_date = models.DateTimeField(default = timezone.now)
	discussion = models.ForeignKey(Discussion)

	def __str__(self):
		return self.title