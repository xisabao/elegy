from django import forms
from .models import Post, Assignment

class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ('title', 'text')

class AssignmentForm(forms.ModelForm):

	class Meta:
		model = Assignment
		fields = ('title', 'description')