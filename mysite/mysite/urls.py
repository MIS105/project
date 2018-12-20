"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from musicer.views import hello_world
from musicer.views import home
from musicer.views import activity_detail
from musicer.views import addActivity
from musicer.views import search


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/',hello_world, name='hello_world'),
	path('',addActivity,name='addActivity'),
	re_path(r'activity/(?P<pk>\d+)/', activity_detail, name='activity_detail'),
    path('search/',search,name='search'),
]
