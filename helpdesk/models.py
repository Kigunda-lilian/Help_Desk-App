from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.urls import reverse
# from notifications.models import Notification

class Profile(models.Model):
    prof_pic = models.ImageField(upload_to='images/', default='default.png')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    def __str__(self):
        return f'{self.user.username} Profile'


import datetime as dt
class Post(models.Model):
    post_owner = models.ForeignKey(User, on_delete=models.PROTECT,null="False",related_name='user_images')
    title = models.CharField(max_length=40)
    question=models.TextField(max_length=280)
    tag=models.ManyToManyField('Tag', blank=True, related_name='tag')
    posted_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='dislikes')
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
            return self.title
    
       
class Tag(models.Model):
    language= models.CharField(max_length=50)
    stage= models.CharField(max_length=80)
    title=models.CharField(max_length=50)
    Description=models.TextField()
    quiz = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='query',null="True")
    logical=models.BooleanField(default=True)
    technical=models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.language
    
reactions={('Like','Like'),('Unlike','Unlike')}
    
class Comment(models.Model):
     post = models.ForeignKey(Post,related_name="comments" ,null=True,on_delete=models.CASCADE)
     user=models.ForeignKey(User,on_delete=models.CASCADE)
     body = models.TextField(max_length=500)
     date= models.DateTimeField(auto_now_add=True)
     agreed = models.BooleanField('Agreed',default=False)
     likes = models.ManyToManyField(User, blank=True, related_name='comment_likes'),
     dislikes = models.ManyToManyField(User, blank=True, related_name='comment_dislikes')
     total_likes=models.IntegerField(default=0)
     total_dislikes=models.IntegerField(default=0)

     def __str__(self):
         return '{}-{}'.format(self.post.title, str(self.user.username))
        
     
    
    
class Like(models.Model):
    response = models.CharField(choices=reactions,null=True,max_length=70)
    user = models.ForeignKey(User,null=True,on_delete = models.CASCADE)
    comment=models.ForeignKey(Comment,null=True,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.response
class Dislike(models.Model):
    response = models.CharField(choices=reactions,null=True,max_length=70)
    user = models.ForeignKey(User,null=True,on_delete = models.CASCADE)
    comment=models.ForeignKey(Comment,null=True,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.response




