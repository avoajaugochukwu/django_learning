from django.conf.urls import patterns, include, url
from django.contrib import admin
from r_project import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'r_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^rango/', include('rango.urls')),
)
