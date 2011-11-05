from django.conf.urls.defaults import patterns, include, url
from dreamspace.views import all, posting

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       ('^$', all ),
                       ('^posting$', posting ),
    # Examples:
    # url(r'^$', 'dreamspace.views.home', name='home'),
    # url(r'^dreamspace/', include('dreamspace.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
