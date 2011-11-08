from django.db import models

class Post( models.Model ):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    public = models.BooleanField()
    time = DateTimeField( auto_now_add=True )
    user = models.CharField(max_length=30)
    
    def __unicode( self ):
        return self.title
