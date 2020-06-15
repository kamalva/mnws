"""mnws URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url, include
from wpb import views
from .views import HomePageView, SearchResultsView
app_name = 'wpb'

urlpatterns = [
    url(r'^politics/$',views.politics,name='politics'),
    url(r'^politics/cts/',views.cts,name='cts'),
    url(r'^index/$',views.index,name='index'),
    url(r'^contactus/$', views.contactus, name='contactus'),
    url(r'^about/$', views.about, name='about'),
    url(r'^search/$', SearchResultsView.as_view(), name='search'),
    url(r'^search/politics/cts/',views.cts,name='cts'),
    url(r'^psych/$',views.psych,name='psych'),
    url(r'^thil/$',views.thil,name='thil'),


]
