from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from dreamspace.blog.models import Post, Like
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.core.context_processors import csrf

def home( request ):
    inGuy = isAuthUser( request )
    posts = Post.objects.all().order_by( 'time' )
    users = User.objects.all()
    return render_to_response( 'index.html', locals() )

def profile( request, person=None):
    inGuy = isAuthUser( request )
    try:
        owner = person if person else inGuy
        U = User.objects.get( username=owner )
        posts = Post.objects.filter(user=U)
        return render_to_response( 'profile.html', locals() )
    except:
        return render_to_responseC( request, '404.html', locals () )

def posts( request, postid ):
    inGuy = isAuthUser( request )
    try:
        post = Post.objects.get( id=postid )
        posts = [ post ]
    except:
        return render_to_responseC( request, '404.html', locals () )
    liked = Like.objects.filter( user=request.user, post=post )
    if inGuy and request.method == 'POST' and not liked:
        Like( user=request.user, post=post ).save()
        post.likes += 1
        post.save()
    return render_to_responseC( request, 'posts.html', locals() )

def delete( request, postid ):
    inGuy = isAuthUser( request )
    try:
        post = Post.objects.get( id=postid )
        if post.user.username == inGuy:
            post.delete()
            success = "Post was successfully deleted"
        else:
            failure = "You cannot delete some one else's post..., nice try"
        return render_to_responseC( request, 'result.html', locals () )
    except:
        return render_to_responseC( request, '404.html', locals () )

def posting( request ):
    inGuy = isAuthUser( request )
    if request.method == 'POST':
        title, content, public = request.POST[ 'title' ], request.POST[ 'content' ], request.POST.get( 'public', False )
        alreadyPosted = Post.objects.filter( title=title, content=content, user=request.user )
        if title and content and not alreadyPosted:
            post = Post( title=title, content=content, user=request.user, public=public, likes=0 )
            post.save()
            success = "Post was successfully created"
            return render_to_responseC( request, 'result.html', locals() )
        else:
            errors = [ "There was something wrong with your post" ]
            titleError, contentError = not title, not content
    return render_to_responseC( request, 'posting.html', locals() )

def edit( request, postid ):
    inGuy = isAuthUser( request )
    try:
        post = Post.objects.get( id=postid )
    except:
        return render_to_responseC( request, '404.html', locals () )
    if request.method == 'POST':
        title, content, public = request.POST[ 'title' ], request.POST[ 'content' ], bool( request.POST.get( 'public', False ) )
        if inGuy == post.user.username and title and content:
            post.title, post.content, post.public = title, content, public
            post.save()
            success = "Your post has been succesfully saved"
            return render_to_responseC( request, 'result.html', locals() )
        else:
            errors = [ "There was something wrong with your post" ]
            titleError, contentError = not title, not content
    if post.user.username == inGuy:
        return render_to_responseC( request, 'posting.html', locals () )
    else:
        failure = "You cannot edit someone else's post, nice try.."
        return render_to_responseC( request, 'result.html', locals () )

def about( request ):
    inGuy = isAuthUser( request )
    return render_to_response( 'about.html', locals() )

def register( request ):
    if request.method == 'POST':
        form = UserCreationForm( request.POST )
        if form.is_valid():
            new_user = form.save()
            return render_to_responseC( request, 'result.html', locals() )
    else:
        form = UserCreationForm()
    return render_to_responseC( request, "registration/register.html", locals() )


# Helper procedures
def render_to_responseC( request, link, context ):
    context.update( csrf( request ) )
    return render_to_response( link, context )

def isAuthUser( request ):
    return request.user.username if request.user.is_authenticated() else None
# End of Helper procedures
