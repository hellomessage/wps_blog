"""wpsblog URL Configuration

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
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from wpsblog.views import home, room, news
 
# MVC
# M Business Loginc
# v template/client
# C View, Model

# Model => 더 무겁게
# Contriller => 더 가볍게 (즉 기능이 Contriller => Model.....)

urlpatterns = [
    url(r'^admin/', admin.site.urls),

	url(r'^$', home, name="home"),
	url(r'^rooms/(?P<room_id>\d+)/$', room, name="room"),
	url(r'^news/$', news, name="news"),
]
