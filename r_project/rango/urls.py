from django.conf.urls import patterns, include, url
from rango import views
# for uploading files
from django.conf import settings

urlpatterns = patterns('',
		url(r'^$', views.index, name='index'),
		url(r'^about$', views.about),
		url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
	)

if settings.DEBUG:
	urlpatterns += patterns(
			'django.views.static',
			(r'^media/(<?path>.*)',
				'serve',
				{'document_root': settings.MEDIA_ROOT}),

		)