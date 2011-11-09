from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from dreamspace.blog.models import Post
from django.shortcuts import render_to_response
from django.core.context_processors import csrf



def home( request ):
    inGuy = isAuthUser( request )
    posts = Post.objects.all().order_by( 'time' )
    users = User.objects.all()
    return render_to_response( 'index.html', locals() )

def profile( request, person=None):
    inGuy = isAuthUser( request )
    owner = person if person else inGuy
    try:
        posts = Post.objects.filter(user=owner).order_by( 'time' )
        return render_to_response( 'profile.html', locals() )
    except:
        pass

def posts( request, postid ):
    inGuy = isAuthUser( request )
    try:
        post = Post.objects.get( id=postid )
        posts = [ post ]
        return render_to_response( 'posts.html', locals() )
    except:
        return render_to_responseC( request, '404.html', locals () )

def delete( request, postid ):
    inGuy = isAuthUser( request )
    try:
        post = Post.objects.get( id=postid )
        if post.user == inGuy:
            post.delete()
            success = "Post was successfully deleted"
            return render_to_responseC( request, 'result.html', locals () )
        else:
            failure = "You cannot delete some one else's post..., nice try"
            return render_to_responseC( request, 'result.html', locals () )
    except:
        return render_to_responseC( request, '404.html', locals () )

def posting( request ):
    inGuy = isAuthUser( request )
    if request.method == 'POST':
        title, content, public = request.POST[ 'title' ], request.POST[ 'content' ], request.POST.get( 'public', False )
        if title and content:
            Post( title=title, content=content, user=request.user.username, public=public ).save()
            success = "Post was successfully created"
            return render_to_responseC( request, 'result.html', locals() )
        else:
            errors = [ "There was something wrong with your post" ]
            if not title: errors += [ "* You need a title in your post" ]
            if not content: errors += [ "* You need some content in your post" ]
    return render_to_responseC( request, 'posting.html', locals() )

def edit( request, postid ):
    inGuy = isAuthUser( request )
    try:
        post = Post.objects.get( id=postid )
    except:
        return render_to_responseC( request, '404.html', locals () )
    if request.method == 'POST':
        title, content, public = request.POST[ 'title' ], request.POST[ 'content' ], bool( request.POST.get( 'public', False ) )
        if inGuy == post.user and title and content:
            post.title, post.content, post.public = title, content, public
            post.save()
            success = "Your post has been succesfully saved"
            return render_to_responseC( request, 'result.html', locals() )
        else:
            errors = [ "There was something wrong with your post" ]
            titleError, contentError = not title, not content
    if post.user == inGuy:
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
            return HttpResponseRedirect( '/success' )
    else:
        form = UserCreationForm()
    return render_to_responseC( request, "registration/register.html", locals() )

def success( request ):
    return render_to_response( 'result.html' )


# Helper procedures
def render_to_responseC( request, link, context ):
    context.update( csrf( request ) )
    return render_to_response( link, context )

def isAuthUser( request ):
    return request.user.username if request.user.is_authenticated() else None
# End of Helper procedures
