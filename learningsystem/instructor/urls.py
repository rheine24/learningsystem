from django.conf.urls import patterns, url
from instructor import views

urlpatterns = patterns('',
        url(r'^$', views.home, name='home'),
        url(r'^home/', views.home, name = 'home')
             
        )