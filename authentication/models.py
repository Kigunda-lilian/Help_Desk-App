from django.db import models
from django.contrib.auth.models import User
import datetime as dt

# Create your models here.
class Tag(models.Model):
    language= models.CharField(max_length=50)
    stage= models.CharField(max_length=80)
    logical=models.BooleanField(default=True)
    technical=models.BooleanField(default=False)
    
    def __str__(self):
        return self.language
    
reactions={('Like','Like'),('Unlike','Unlike')}
    
class Comments(models.Model):
    post = models.ForeignKey(Post,related_name="comments" ,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete = models.CASCADE,related_name='comments')
    name = models.CharField(max_length=255)
    reply = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
         return '%s - %s' % (self.post.title, self.name)
    
    

   
    
    
    

