from django.conf.urls import patterns, include, url
from aws_test import views
# for uploading files
from django.conf import settings

urlpatterns = patterns('',
		url(r'^$', views.index, name='index'),

	)