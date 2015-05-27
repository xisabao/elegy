from django import forms
from django.contrib.auth.models import User
from .models import Post, Assignment, Student, Teacher, StudentToClass, TeacherToClass, Discussion, DiscussionPosts

class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ('title', 'text')

class AssignmentForm(forms.ModelForm):

	class Meta:
		model = Assignment
		fields = ('title', 'description')

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
	class Meta:
		model = Student
		fields = ('theclass',)
		widgets = {
			'theclass': forms.CheckboxSelectMultiple(),
		}

class TeacherForm(forms.ModelForm):
	class Meta:
		model = Teacher
		fields = ('theclass',)
		widgets = {
		'theclass': forms.CheckboxSelectMultiple(),
		}