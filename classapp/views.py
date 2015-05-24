from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import TheClass, Post, Assignment
from .forms import PostForm, AssignmentForm

# Create your views here.
def class_list(request):
	classes = TheClass.objects.all()
	return render(request, 'classapp/class_list.html', {'classes': classes})

def classpage(request, theclass):
	posts = Post.objects.filter(theclass = theclass)
	assignments = Assignment.objects.filter(theclass = theclass)
	return render(request, 'classapp/classpage.html', {'theclass': theclass, 'posts': posts, 'assignments': assignments})

def postpage(request, pk, theclass):
	post = Post.objects.get(id = pk, theclass = theclass)
	return render(request, 'classapp/postpage.html', {'post': post})

def assignmentpage(request, pk, theclass):
	assignment = Assignment.objects.get(id=pk, theclass = theclass)
	return render(request, 'classapp/assignmentpage.html', {'assignment': assignment})

def post_new(request, theclass):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.theclass = TheClass.objects.get(id = theclass)
			post.save()
			return redirect('classapp.views.postpage', pk=post.pk, theclass=theclass)
	else:
		form = PostForm()
	return render(request, 'classapp/post_edit.html', {'form': form})

def assignment_new(request, theclass):
	if request.method == "POST":
		form = AssignmentForm(request.POST)
		if form.is_valid():
			assignment = form.save(commit=False)
			assignment.theclass = TheClass.objects.get(id = theclass)
			assignment.save()
			return redirect('classapp.views.assignmentpage', pk=assignment.pk, theclass=theclass)
	else:
		form = AssignmentForm
	return render(request, 'classapp/assignment_edit.html', {'form': form})

def post_edit(request, pk, theclass):
	post = Post.objects.get(pk=pk, theclass=theclass)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('classapp.views.postpage', pk = post.pk, theclass=theclass)
	else:
		form = PostForm(instance=post)
	return render(request, 'classapp/post_edit.html', {'form': form})

def assignment_edit(request, pk, theclass):
	assignment = Assignment.objects.get(pk=pk, theclass = theclass)
	if request.method == "POST":
		form = AssignmentForm(request.POST, instance=assignment)
		if form.is_valid():
			assignment = form.save(commit=False)
			assignment.save()
			return redirect('classapp.views.assignmentpage', pk=assignment.pk, theclass = theclass)
	else:
		form = AssignmentForm(instance=assignment)
	return render(request, 'classapp/assignment_edit.html', {'form': form})