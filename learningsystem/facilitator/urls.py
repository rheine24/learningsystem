from django.conf.urls import patterns, url
from facilitator import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='facIndex')
        )