"""restful_tv_shows URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to ur,lpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views 


urlpatterns = [
    url('shows', views.index),
    url('add_show', views.add_show),
    url('submit_show', views.submit_show),
    url('^display_show/(?P<id>\d)$', views.display_show),
    url('^edit_show/(?P<id>\d)', views.edit_show),
    url('^submit_edit/(?P<id>\d)', views.submit_edit),
    url('^delete_show/(?P<id>\d)', views.delete_show),
]

