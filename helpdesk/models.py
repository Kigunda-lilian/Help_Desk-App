from django.db import models
from authentication.models import Account
from django.db.models.signals import post_save, post_delete
from django.urls import reverse
# from notifications.models import Notification

class Profile(models.Model):
    prof_pic = models.ImageField(upload_to='images/', default='default.png')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    user = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='profile')
    def __str__(self):
        return f'{self.user.username} Profile'


import datetime as dt
class Post(models.Model):
    post_owner = models.ForeignKey(Account, on_delete=models.PROTECT,null="False",related_name='user_images')
    title = models.CharField(max_length=40)
    question=models.TextField(max_length=280)
    tag=models.ManyToManyField('Tag', blank=True, related_name='tag')
    posted_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(Account, blank=True, related_name='likes')
    dislikes = models.ManyToManyField(Account, blank=True, related_name='dislikes')
   
    def create_post(self):
            self.save()

    def delete_post(self):
        self.delete()
        
    def update_post(self):
            self.update()

    def get_absolute_url(self):
        return reverse('questions')
        
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
             return '{}-{}'.format(self.title, str(self.tag.language))
       
    
       
class Tag(models.Model):
    language= models.CharField(max_length=50)
    stage= models.CharField(max_length=80)
    
    
    logical=models.BooleanField(default=True)
    technical=models.BooleanField(default=False)
    
    def __str__(self):
        return self.language
    
reactions={('Like','Like'),('Unlike','Unlike')}
    
class Comments(models.Model):
     post = models.ForeignKey(Post,related_name="comments" ,null=True,on_delete=models.CASCADE)
     user=models.ForeignKey(Account,on_delete=models.CASCADE,null="False")
     body = models.TextField(max_length=500)
     date= models.DateTimeField(auto_now_add=True)
     agreed = models.BooleanField('Agreed',default=False)

     def __str__(self):
         return '{}-{}'.format(self.post.title, str(self.user.username))
    
    
    
class Like(models.Model):
    response = models.CharField(choices=reactions,default='like',max_length=70)
    user = models.ForeignKey(Account,on_delete = models.CASCADE,null="False")
    
    def __str__(self):
        return self.response
