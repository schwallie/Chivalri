from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^usercp/', include('usercp.urls')),
     url(r'^register/', 'Chivalri.views.register'),
    url(r'^accounts/login/$','django.contrib.auth.views.login'),
    url(r'^login/$','django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^$', 'Chivalri.views.home', name='home'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
