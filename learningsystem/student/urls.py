from django.conf.urls import patterns, url
from student import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='studIndex'),
        url(r'^test',views.test,name = 'studTest'))