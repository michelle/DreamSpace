from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from dreamspace.blog.models import Post
from django.shortcuts import render_to_response
from django.core.context_processors import csrf

# Helper procedures
def render_to_responseC( request, link, context ):
    context.update( csrf( request ) )
    return render_to_response( link, context )

def isAuthUser( request ):
    return request.user.username if request.user.is_authenticated() else None

# End of Helper procedures

# Star of Views        
def home( request ):
    import os
    username = isAuthUser( request )
    posts = Post.objects.all().order_by( 'created' )
    users = User.objects.all()
    assert False, ( os.listdir( '/' ),
                    os.listdir( '/app' ),
                    os.listdir( 'app/dreamspace' ),
                    os.listdir( 'app/dreamspace/dreamspace' ), )
    return render_to_response( 'index.html', locals() )


def profile( request, person=None):
    username = isAuthUser( request )
    profile = person[:-1] if person else username
    if profile:
        posts = Post.objects.filter(user=profile).order_by( 'created' )
    else:
        errors = True
    return render_to_response( 'profile.html', locals() )

def register( request ):
    if request.method == 'POST':
        form = UserCreationForm( request.POST )
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect( '/success' )
    else:
        form = UserCreationForm()
    return render_to_responseC( request, "registration/register.html", locals() )

def posting( request ):
    username = isAuthUser( request )
    if request.method == 'POST':
        title = request.POST[ 'title' ]
        content = request.POST[ 'content' ]
        if username and title and content:
            Post( title=title, content=content, user=request.user.username ).save()
            success = "Post was successfully created"
            return render_to_responseC( request, 'success.html', locals() )
    return render_to_responseC( request, 'posting.html', locals() )

def success( request ):
    return render_to_response( 'success.html' )

