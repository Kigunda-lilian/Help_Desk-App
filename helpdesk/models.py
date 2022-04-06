
from django.db import models
from authentication.models import Account

import datetime as dt

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(Account, on_delete=models.PROTECT,null="False",related_name='user_images')
    name = models.CharField(max_length=40)
    question=models.TextField(max_length=280)
    posted_on = models.DateTimeField(auto_now_add=True)
    liked= models.ManyToManyField(Account,default=None,blank=True,related_name='liked')
    comment = models.IntegerField(blank=True,null=True,default=True)
    tag_title=models.ForeignKey("Tag",on_delete = models.PROTECT,null="False")
    answers= models.ForeignKey('Comments',on_delete = models.CASCADE)
    postslikes= models.IntegerField(blank=True,null=True,default=True)
    
    

    
    def create_post(self):
            self.save()

    def delete_post(self):
        self.delete()
        
    def update_post(self):
            self.update()
        
    @classmethod
    def search_by_name(cls, search_term):
        posts = cls.objects.filter(name__icontains=search_term)
        return posts
    
    @classmethod
    def find_post(cls, id):
        post = cls.objects.get(id=id)
        return post
    
    class Meta:
        ordering = ['posted_on']
        
    @property
    def saved_comments(self):
        return self.comments.all()
    
    @property
    def saved_likes(self):
      return self.postslikes.count()
  
    def __str__(self):
            return self.name
    
       
class Tag(models.Model):
    language= models.CharField(max_length=50)
    stage= models.CharField(max_length=80)
    title=models.CharField(max_length=50,null="False")
    Description=models.TextField()
    # quiz = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='query',null="True")
    logical=models.BooleanField(default=True)
    technical=models.BooleanField(default=False)
    
    def __str__(self):
        return self.language
    
reactions={('Like','Like'),('Unlike','Unlike')}
    
class Comments(models.Model):
    question = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(Account,on_delete = models.CASCADE,null="False")
    name = models.CharField(max_length=255)
    reply = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
         return '%s - %s' % (self.post.name, self.name)
    
    
class Like(models.Model):
    response = models.CharField(choices=reactions,default='like',max_length=70)
    user = models.ForeignKey(Account,on_delete = models.CASCADE,null="False")
    
    def __str__(self):
        return self.response
    

   
    
    
    

