from django.db import models

class User( models.Model ):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    
    def __unicode__( self ):
        return self.name

class Post( models.Model ):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    # public = models.BooleanField()
    # time = models.DateField()
    # user = models.ForeignKey( User )
    
    def __unicode( self ):
        return self.title
