from django.conf.urls import patterns, url
from instructor import views

urlpatterns = patterns('',
        url(r'^$', views.home, name='InsIndex'),
        url(r'^home/', views.home, name = 'InsHome'),
        url(r'^confirmevent/',views.confirmEvent, name = 'InsConfirm'),
        url(r'^saveevent/',views.saveEvent, name = 'InsSave'),
        url(r'^details/',views.about, name = 'InsAbt')
             
        )