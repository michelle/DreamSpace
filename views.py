from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from dreamspace.blog.models import Post
from django.shortcuts import render_to_response
from collections import namedtuple
import datetime
from django.core.context_processors import csrf

def render_to_responseC( request, link, context ):
    context.update( csrf( request ) )
    return render_to_response( link, context )

def all( request ):
    ctx = { 'posts' : Post.objects.all().order_by( 'created' ) }
    if request.user.is_authenticated():
        ctx[ 'username' ] = request.user.username
        ctx[ 'loggedIn' ] = True
    return render_to_response( 'all.html', ctx )

def profile( request ):
    posts = Post.objects.all().order_by( 'created' )
    return render_to_response( 'all.html', {'posts' : posts } )

def register( request ):
    if request.method == 'POST':
        form = UserCreationForm( request.POST )
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect( '../success' )
    else:
        form = UserCreationForm()
    return render_to_responseC( request, "registration/register.html", { 'form': form } )

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

def success( request ):
    return render_to_response( 'success.html' )

def drop( request ):
    Post.objects.all().delete()
    return render_to_response( 'dropped.html' )
