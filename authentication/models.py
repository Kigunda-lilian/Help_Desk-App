from turtle import title
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
import datetime as dt

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT,related_name='user_images')
    name = models.CharField(max_length=40)
    question=models.TextField(max_length=280)
    posted_on = models.DateTimeField(auto_now_add=True)
    liked= models.ManyToManyField(User,default=None,blank=True,related_name='liked')
    comment = models.IntegerField(blank=True,null=True,default=True)
    tag=models.ForeignKey(User,on_delete = models.PROTECT)
    comments= models.ForeignKey(Comments,on_delete = models.CASCADE,related_name='comments')
    postslikes= models.IntegerField(blank=True,null=True,default=True)
    
    def create_post(self):
            self.save()

    def delete_post(self):
        self.delete()

    
       
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
         return '%s - %s' % (self.post.name, self.name)
    
    
class Like(models.Model):
    response = models.CharField(choices=reactions,default='like',max_length=70)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    
    def __str__(self):
        return self.response
    

   
    
    
    

