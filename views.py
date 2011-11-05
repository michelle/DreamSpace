from django.http import HttpResponse
from django.template import Template, Context, RequestContext
from dreamspace.blog.models import Post
from django.shortcuts import render_to_response
from collections import namedtuple
import datetime

def all( request ):
    posts = Post.objects.all().order_by( 'created' )
    return render_to_response( 'all.html', {'posts' : posts } )

def posting( request ):
    return render_to_response( 'posting.html' )

def posted( request ):
    if 'title' in request.GET and 'content' in request.GET:
        title = request.GET[ 'title' ]
        content = request.GET[ 'content' ]
        Post( title=title, content=content ).save()
    else:
        pass
    return render_to_response( 'posted.html' )

def drop( request ):
    Post.objects.all().delete()
    return render_to_response( 'dropped.html' )
