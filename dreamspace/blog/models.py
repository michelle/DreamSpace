from django.db import models
from django.contrib.auth.models import User

class Like( models.Model ):
    post = models.ForeignKey('Post')
    user = models.ForeignKey(User)

class Post( models.Model ):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    public = models.BooleanField()
    time = models.DateTimeField( auto_now_add=True )
    user = models.ForeignKey(User)
    likes = models.PositiveSmallIntegerField()

    def __unicode( self ):
        return self.title


