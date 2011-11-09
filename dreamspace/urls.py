from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
import dreamspace.views as vs
from dreamspace.blog.views import gen
from django.contrib.auth.views import login, logout
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       ('^$', vs.home ),
                       ('^about/$', vs.about ),
                       ('^posting/$', vs.posting ),
                       ('^register/$', vs.register ),
                       ('^login/$', login ),
                       ('^logout/$', logout ),
                       (r'^profile/(\w+)?/?$', vs.profile ),
                       (r'^posts/(\d+)/$', vs.posts ),
                       (r'^posts/(\d+)/edit/$', vs.edit ),
                       (r'^posts/(\d+)/delete/$', vs.delete ),
                       ('^gen/', gen ),
                       url(r'^admin/', include(admin.site.urls)),
)

