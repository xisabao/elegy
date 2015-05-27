from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^classes$', views.class_list, name="class_list"),
	url(r'^classes/(?P<theclass>[0-9]+)/$', views.classpage, name="classpage"),
	url(r'^classes/(?P<theclass>[0-9]+)/post/(?P<pk>[0-9]+)/$', views.postpage, name="postpage"),
	url(r'^classes/(?P<theclass>[0-9]+)/post/$', views.post_list, name="post_list"),
	url(r'^classes/(?P<theclass>[0-9]+)/assignment/$', views.assignment_list, name="assignment_list"),
	url(r'^classes/(?P<theclass>[0-9]+)/assignment/(?P<pk>[0-9]+)/$', views.assignmentpage, name = "assignmentpage"),
	url(r'^classes/(?P<theclass>[0-9]+)/post/new/$', views.post_new, name="post_new"),
	url(r'^classes/(?P<theclass>[0-9]+)/assignment/new/$', views.assignment_new, name="assignment_new"),
	url(r'^classes/(?P<theclass>[0-9]+)/post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name="post_edit"),
	url(r'^classes/(?P<theclass>[0-9]+)/assignment/(?P<pk>[0-9]+)/edit/$', views.assignment_edit, name="assignment_edit"),
	url(r'^register_student/$', views.register_student, name="register_student"),
	url(r'^register_teacher/$', views.register_teacher, name="register_teacher"),
	url(r'^login/$', views.user_login, name="login"),
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^classes/(?P<theclass>[0-9]+)/discussions/$', views.discussion_list, name="discussion_list"),
	url(r'^classes/(?P<theclass>[0-9]+)/discussions/(?P<pk>[0-9]+)/$', views.discussionpage, name="discussionpage"),
	url(r'^classes/(?P<theclass>[0-9]+)/discussions/new/$', views.discussion_new, name="discussion_new"),
	url(r'^classes/(?P<theclass>[0-9]+)/discussions/(?P<pk>[0-9]+)/new/$', views.discussionpost_new, name="discussionpost_new"),
]