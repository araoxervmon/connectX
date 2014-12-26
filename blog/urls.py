__author__ = 'Abhilash'
from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^admin/', include(admin.site.urls)),


    url(r'', 'app.view.index'),
  #  url(r'^', ListView.as_view(queryset=Post.objects.all().orderby("created"[:2], template_name="blog.html")))
)
