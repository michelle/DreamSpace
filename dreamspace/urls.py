from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from dreamspace.views import *
from django.contrib.auth.views import login, logout
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

def gen( request ):
    for user, pw1 in ( ('rising', 'foobar' ),
                       ('fallen','foobar' ),
                       ('dreamz','foobar' ) ):
        if not User.objects.filter( username=user ):
            User( username=user, password=pw1 ).save()
    for user, title, content, public in ( ( 'rising', 'rosen', 'last night I dreamt of flying in the sky', True ),
                                          ( 'fallen', 'fell', 'last night I dreamt that I was falling and woke up upruptly', True ),
                                          ( 'dreamz', 'dreamy', 'last night I dreamt of a dreamy boy in class', False ) ):
        if not Post.objects.filter( content=content ):
            Post( title=title, content=content, user=user, public=public ).save()
    return HttpResponse( 'itz done' )


urlpatterns = patterns('',
                       ('^$', home ),
                       ('^about/$', about ),
                       ('^posting/$', posting ),
                       ('^register/$', register ),
                       ('^success/$', success ),
                       ('^login/$', login ),
                       ('^logout/$', logout ),
                       (r'^profile/(\w+)?/?$', profile ),
                       (r'^posts/(\d+)/$', posts ),
                       (r'^posts/(\d+)/edit/$', edit ),
                       (r'^posts/(\d+)/delete/$', delete ),
                       ('^gen/', gen ),
                       url(r'^admin/', include(admin.site.urls)),
)

