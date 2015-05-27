from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.template import RequestContext
from django.shortcuts import render, redirect, render_to_response
from django.utils import timezone
from .models import TheClass, Post, Assignment, Teacher, Student, Discussion, DiscussionPosts
from .forms import PostForm, AssignmentForm, UserForm, StudentForm, TeacherForm, DiscussionForm, DiscussionPostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password

def student_in_class(user, theclasspk, studentmodel, classmodel):
	if user:
		primary_key = user.pk
		student = studentmodel.objects.get(user = primary_key)
		if student:
			if classmodel.objects.get(pk = theclasspk) in student.theclass.all():
				return True
			else:
				return False
		else:
			return False
	else:
		return False

def teacher_in_class(user, theclasspk, teachermodel, classmodel):
	if user:
		primary_key = user.pk
		teacher = teachermodel.objects.get(user = primary_key)
		if teacher:
			if classmodel.objects.get(pk = theclasspk) in teacher.theclass.all():
				return True
			else:
				return False
		else:
			return False
	else:
		return False

################################################# VIEWS ##################################
def index(request):
	return render(request, 'classapp/index.html', {})

@login_required
def class_list(request):
	primary_key = request.user.pk 
	
	try:
		student = Student.objects.get(user = primary_key)
		classes = student.theclass.all()
	except:
		teacher = Teacher.objects.get(user = primary_key)
		classes = teacher.theclass.all()
	return render(request, 'classapp/class_list.html', {'classes': classes})

@login_required
def classpage(request, theclass):
		try: 
			if student_in_class(request.user, theclass, Student, TheClass):
				posts = Post.objects.filter(theclass = theclass).order_by('-published_date')[:5]
				assignments = Assignment.objects.filter(theclass = theclass).order_by('-due_date')[:5]
				return render(request, 'classapp/classpage.html', {'theclass': theclass, 'posts': posts, 'assignments': assignments})
		except:
		 	if teacher_in_class(request.user, theclass, Teacher, TheClass):
		 		posts = Post.objects.filter(theclass = theclass).order_by('-published_date')[:5]
				assignments = Assignment.objects.filter(theclass = theclass).order_by('-due_date')[:5]
				return render(request, 'classapp/classpage.html', {'theclass': theclass, 'posts': posts, 'assignments': assignments})
		return redirect('classapp.views.class_list')

@login_required
def post_list(request, theclass):
	posts = Post.objects.filter(theclass = theclass)
	return render(request, 'classapp/post_list.html', {'posts': posts, 'theclass': theclass})

@login_required
def postpage(request, pk, theclass):
	post = Post.objects.get(id = pk, theclass = theclass)
	return render(request, 'classapp/postpage.html', {'post': post, 'theclass': theclass})

@login_required
def assignment_list(request, theclass):
	assignments = Assignment.objects.filter(theclass = theclass)
	return render(request, 'classapp/assignment_list.html', {'assignments': assignments, 'theclass': theclass})

@login_required
def assignmentpage(request, pk, theclass):
	assignment = Assignment.objects.get(id=pk, theclass = theclass)
	return render(request, 'classapp/assignmentpage.html', {'assignment': assignment, 'theclass': theclass})

@login_required
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

@login_required
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

@login_required
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
	return render(request, 'classapp/post_edit.html', {'form': form, 'theclass': theclass, 'pk': pk})
@login_required
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
	return render(request, 'classapp/assignment_edit.html', {'form': form, 'theclass': theclass, 'pk': pk})

@login_required
def discussion_list(request, theclass):
	discussions = Discussion.objects.filter(theclass = theclass).order_by('created_date')
	return render(request, 'classapp/discussion_list.html', {'discussions': discussions, 'theclass': theclass})

@login_required
def discussionpage(request, theclass, pk):
	posts = DiscussionPosts.objects.filter(discussion = pk).order_by('published_date')
	return render(request, 'classapp/discussionpage.html', {'posts': posts, 'theclass': theclass, 'pk': pk})

@login_required
def discussion_new(request, theclass):
	if request.method == "POST":
		form = DiscussionForm(request.POST)
		if form.is_valid():
			discussion = form.save(commit=False)
			discussion.creator = request.user
			discussion.theclass = TheClass.objects.get(id = theclass)
			discussion.save()
			return redirect('classapp.views.discussionpage', pk=discussion.pk, theclass=theclass)
	else:
		form = DiscussionForm()
	return render(request, 'classapp/discussion_edit.html', {'form': form, 'theclass': theclass})

@login_required
def discussionpost_new(request, theclass, pk):
	if request.method == "POST":
		form = DiscussionPostForm(request.POST)
		if form.is_valid():
			discussionpost = form.save(commit=False)
			discussionpost.author = request.user
			discussionpost.discussion = Discussion.objects.get(pk = pk)
			discussionpost.save()
			return redirect('classapp.views.discussionpage', pk=pk, theclass=theclass)
	else:
		form = DiscussionPostForm()
	return render(request, 'classapp/discussionpost_edit.html', {'form': form, 'theclass': theclass, 'pk': pk})


################################## Auth stuff ##########################################

def register_student(request):
	context = RequestContext(request)
	registered = False
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		student_form = StudentForm(data = request.POST)

		if user_form.is_valid() and student_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)

			user.save()

			student = student_form.save(commit = False)
			student.user = user
			student.save()
			registered = True
	else:
		user_form = UserForm()
		student_form = StudentForm()
	return render_to_response('classapp/register_student.html', {'user_form': user_form, 'student_form': student_form, 'registered': registered}, context)

def register_teacher(request):
	context = RequestContext(request)
	registered = False
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		teacher_form = TeacherForm(data = request.POST)

		if user_form.is_valid() and teacher_form.is_valid():

			user = user_form.save()

			user.set_password(user.password)

			user.save()

			teacher = teacher_form.save(commit = False)
			teacher.user = user
			teacher.save()
			registered = True
	else:
		user_form = UserForm()
		teacher_form = TeacherForm()
	return render_to_response('classapp/register_teacher.html', {'user_form': user_form, 'teacher_form': teacher_form, 'registered': registered}, context)

def user_login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username = username, password = password)

		if user:
			if user.is_active:
				login(request, user)
				return redirect('classapp.views.class_list')
			else:
				return HttpResponse("Your account is disabled.")
		else:
			print "Invalid login details: {0}, {1}".format(username, password)
			return HttpResponse("Invalid login details supplied.")
	else:
		return render(request, 'classapp/login.html', {})

@login_required
def user_logout(request):
	logout(request)

	return redirect('classapp.views.index')