from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from dreamspace.views import *
from django.contrib.auth.views import login, logout
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       ('^$', home ),
                       ('^about/$', about ),
                       ('^posting/$', posting ),
                       ('^register/$', register ),
                       ('^success/$', success ),
                       ('^login/$', login ),
                       ('^logout/$', logout ),
                       (r'^profile/(\w+/)?$', profile ),
    # Examples:
    # url(r'^$', 'dreamspace.views.home', name='home'),
    # url(r'^dreamspace/', include('dreamspace.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
                           url(r'^admin/', include(admin.site.urls)),
)

