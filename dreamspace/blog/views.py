from django.http import HttpResponse
from django.contrib.auth.models import User
from dreamspace.blog.models import Post

def gen( request ):
    users = []
    for user, pw1 in ( ('rising', 'foobar' ),
                       ('fallen','foobar' ),
                       ('dreamz','foobar' ) ):
        if not User.objects.filter( username=user ):
            users.append( User( username=user, password=pw1 ) )
            users[ -1 ].save()
        else:
            users.append( User.objects.get( username=user ) )
    for user, title, content, public in ( ( users[0], 'rosen', 'last night I dreamt of flying in the sky', True ),
                                          ( users[1], 'fell', 'last night I dreamt that I was falling and woke up upruptly', True ),
                                          ( users[2], 'dreamy', 'last night I dreamt of a dreamy boy in class', False ) ):
        if not Post.objects.filter( content=content ):
            Post( title=title, content=content, user=user, public=public, likes=0 ).save()
    return HttpResponse( 'itz done' )

