"""homework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static


urlpatterns = [
    url(r'^wyadmin/', include(admin.site.urls)),
    url(r'^$','work.views.loginForm',name='index'),
    url(r'^userindex$','work.views.userindex',name='usercenter'),
    url(r'^workindex$','work.views.workindex',name='workindex'),
    url(r'^designindex$','work.views.designindex',name='designindex'),
    # url(r'^gethomework$','work.views.gethomework',name='gethomework'),
    # url(r'^getdesign$','work.views.getdesign',name='getdesign'),
    # url(r'^getnewwork$','work.views.newwork',name='newwork'),
    url(r'^addhomework$','work.views.addhomework',name='addhomework'),
    url(r'^adddesign$','work.views.adddesign',name='adddesign'),
    url(r'^passwd$','work.views.passwd',name='passwd'),
    url(r'^logout$','work.views.logout',name='logout'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
