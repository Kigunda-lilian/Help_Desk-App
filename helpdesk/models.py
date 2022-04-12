from django.db import models
from authentication.models import Account

class Profile(models.Model):
    prof_pic = models.ImageField(upload_to='images/', default='default.png')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    user = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='profile')
    def __str__(self):
        return f'{self.user.username} Profile'


import datetime as dt
class Post(models.Model):
    user = models.ForeignKey(Account, on_delete=models.PROTECT,null="False",related_name='user_images')
    title = models.CharField(max_length=40)
    question=models.TextField(max_length=280)
    posted_on = models.DateTimeField(auto_now_add=True)
    comment = models.IntegerField(blank=True,null=True,default=True)
    tag_title=models.CharField(max_length=40,null="False")
    postslikes= models.BooleanField(blank=True,null=True,default=True)
    
    

    
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
        return self.comment.all()
    
    @property
    def saved_likes(self):
      return self.postslikes.count()
  
    def __str__(self):
            return self.title
    
       
class Tag(models.Model):
    language= models.CharField(max_length=50)
    stage= models.CharField(max_length=80)
    title=models.CharField(max_length=50,null="False")
    Description=models.TextField()
    logical=models.BooleanField(default=True)
    technical=models.BooleanField(default=False)
    
    def __str__(self):
        return self.language
    
reactions={('Like','Like'),('Unlike','Unlike')}
    
class Comments(models.Model):
     post = models.ForeignKey(Post,related_name="comments" ,null=True,on_delete=models.CASCADE)
     name=models.CharField(max_length=100)
     body = models.TextField(max_length=500)
     date_added = models.DateTimeField(auto_now_add=True)

     def __str__(self):
         return '%s - %s' % (self.post.title,self.name)
    
    
class Like(models.Model):
    response = models.CharField(choices=reactions,default='like',max_length=70)
    user = models.ForeignKey(Account,on_delete = models.CASCADE,null="False")
    
    def __str__(self):
        return self.response


