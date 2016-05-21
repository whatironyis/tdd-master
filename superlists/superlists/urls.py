"""superlists URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url,patterns,include
from django.contrib import admin
from lists import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
	url(r'^$',views.home_page),
	url(r'^admin/',include(admin.site.urls)),
    url(r'^register/',views.register),
    url(r'^group/', views.group, name='group'),
    url(r'^login/$', views.Login),
    url(r'^logout/$', views.Logout),
    url(r'^new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^delete/$', csrf_exempt(views.post_delete), name='post_delete'),
    url(r'^edit/$', csrf_exempt(views.edit), name='edit'),
    url(r'^todo/$', csrf_exempt(views.todo), name='todo'),
    url(r'^inpro/$', csrf_exempt(views.inpro), name='inpro'),
]
