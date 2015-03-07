from django.conf.urls import patterns, include, url
from rango import views
# for uploading files
from django.conf import settings

urlpatterns = patterns('',
		url(r'^$', views.index, name='index'),
		url(r'^about$', views.about),
		url(r'^add_category/$', views.add_category, name='add_category'),
		url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
		url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
		url(r'^register/$', views.register, name='register'),
		url(r'^login/$', views.user_login, name='login'),
		url(r'^logout/$', views.user_logout, name='logout'),
	)

if settings.DEBUG:
	urlpatterns += patterns(
			'django.views.static',
			(r'^media/(<?path>.*)',
				'serve',
				{'document_root': settings.MEDIA_ROOT}),

		)