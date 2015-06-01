from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.forms import HiddenInput
from django.contrib.auth.models import User
from .models import Post, Assignment, Student, Teacher, StudentToClass, TeacherToClass, Discussion, DiscussionPosts

class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ('title', 'text')

class AssignmentForm(forms.ModelForm):
	due_date = forms.DateField(widget = SelectDateWidget)
	class Meta:
		model = Assignment
		fields = ('title', 'description', 'due_date')

class DiscussionForm(forms.ModelForm):

	class Meta:
		model = Discussion
		fields = ('title', 'description')

class DiscussionPostForm(forms.ModelForm):

	class Meta:
		model = DiscussionPosts
		fields = ('title', 'text')

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ('username', 'email', 'password')


class StudentForm(forms.ModelForm):
	theclass = forms.CharField(widget = HiddenInput(), required=False)
	class Meta:
		model = Student
		fields = ('theclass',)


class TeacherForm(forms.ModelForm):
	theclass = forms.CharField(widget = HiddenInput(), required=False)
	class Meta:
		model = Teacher
		fields = ('theclass',)