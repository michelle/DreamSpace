from django.contrib.auth.models import User

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
    username = isAuthUser( request )
    posts = Post.objects.all().order_by( 'time' )
    users = User.objects.all()
    return render_to_response( 'index.html', locals() )

def profile( request, person=None):
    username = isAuthUser( request )
    profile = person[:-1] if person else username
    if profile:
        posts = Post.objects.filter(user=profile).order_by( 'time' )
    else:
        errors = True
    return render_to_response( 'profile.html', locals() )

def posts( request, postid ):
    username = isAuthUser( request )
    post = Post.objects.get( id=postid )
    title = post.title
    content = post.content
    public = post.public
    user = post.user
    posts = [ post ]
    return render_to_response( 'posts.html', locals() )

def delete( request, postid ):
    username = isAuthUser( request )
    post = Post.objects.get( id=postid )
    if post.user == username:
        post.delete()
        success = "Post was successfully deleted"
        return render_to_responseC( request, 'success.html', locals () )

def edit( request, postid ):
    pass # TODO

def about( request ):
    return render_to_response( 'about.html' )

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
        public = request.POST.get( 'public', False )
        print public
        if username and title and content:
            Post( title=title, content=content, user=request.user.username, public=public ).save()
            success = "Post was successfully created"
            return render_to_responseC( request, 'success.html', locals() )
    return render_to_responseC( request, 'posting.html', locals() )

def success( request ):
    return render_to_response( 'success.html' )

def gen( request ):
    for user, pw1, pw2 in ( ('rising', 'foobar', 'foobar' ),
                            ('fallen', 'foobar', 'foobar' ),
                            ('dreamz', 'foobar', 'foobar' ) ):
        if not User.objects.filter( username=user ):
            User( username=user, password=pw1 ).save()
    for user, title, content, public in ( ( 'rising', 'rosen', 'last night I dreamt of flying in the sky', True ),
                                          ( 'fallen', 'fell', 'last night I dreamt that I was falling and woke up upruptly', True ),
                                          ( 'dreamz', 'dreamy', 'last night I dreamt of a dreamy boy in class', False ) ):
        if not Post.objects.filter( content=content ):
            Post( title=title, content=content, user=user, public=public ).save()
    return HttpResponse( 'itz done' )

