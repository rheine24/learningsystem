from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from learningsystem import views as lsView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', lsView.home, name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login/', lsView.login, name = 'login'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^facilitator/', include('facilitator.urls')),
    url(r'^instructor/', include('instructor.urls')),
    url(r'^registrar/', include('registrar.urls')),
    url(r'^student/', include('student.urls')),
)
