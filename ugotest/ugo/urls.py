from django.conf.urls import patterns, include, url
from ugo import views

urlpatterns = patterns('',
		url(r'^$', views.index, name='index'),
		url(r'^authors/(?P<author_name>[\w\-]+)/$', views.authors, name='authors'),
		url(r'^add_joke/$', views.add_joke, name='add_joke'),
    url(r'^(?P<qd>\w+)/$', views.detail, name='detail'),
)