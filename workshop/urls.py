"""thinkfoss URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
1. Add an import: from my_app import views
2. Add a URL to urlpatterns: url(r'^$', views.home, name='home')
Class-based views
1. Add an import: from other_app.views import Home
2. Add a URL to urlpatterns: url(r'^$', Home.as_view(), name='home')
Including another URLconf
1. Add an import: from blog import urls as blog_urls
2. Add a URL to urlpatterns: url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from register import urls as reg_urls
from register.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),
    url(r'^register/', include(reg_urls)),
    url(r'^user/login/$',
        anonymous_required(auth_views.login),
        {'template_name': 'login.html'},
        name='login'),

    url(r'^user/logout/$',
         auth_views.logout,
         {'template_name': 'logout.html'},
          name='logout'),
    ]