from django.http import HttpResponse
from django.template import Template, Context, RequestContext
from dreamspace.blog.models import Post
from django.shortcuts import render_to_response
from collections import namedtuple

'''
Post = namedtuple( 'Post', ('title', 'content') )
posts.append( Post( "today", "I farted" ) )
posts.append( Post( "yesterday", "I farted" ) )
'''

def all( request ):
    posts = Post.objects.all()#.order_by( 'time' )
    posts = []
    return render_to_response( 'all.html', {'posts' : posts,
                                            } )

def add( request ):
    import datetime
    errors = []
    now = datatime.datetime.now()
    title = postRequest.get( 'title' )
    content = postRequest.get( 'content' )
    if not content:
        error.append( 'Enter some content' )
    if not errors:
        post = Post( title="title", content="content", )
        post.save()
