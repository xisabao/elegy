from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^classes$', views.class_list, name="class_list"),
	url(r'^classes/(?P<theclass>[0-9]+)/$', views.classpage, name="classpage"),
	url(r'^classes/(?P<theclass>[0-9]+)/post/(?P<pk>[0-9]+)/$', views.postpage, name="postpage"),
	url(r'^classes/(?P<theclass>[0-9]+)/assignment/(?P<pk>[0-9]+)/$', views.assignmentpage, name = "assignmentpage"),
	url(r'^classes/(?P<theclass>[0-9]+)/post/new/$', views.post_new, name="post_new"),
	url(r'^classes/(?P<theclass>[0-9]+)/assignment/new/$', views.assignment_new, name="assignment_new"),
	url(r'^classes/(?P<theclass>[0-9]+)/post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name="post_edit"),
	url(r'^classes/(?P<theclass>[0-9]+)/assignment/(?P<pk>[0-9]+)/edit/$', views.assignment_edit, name="assignment_edit"),
]