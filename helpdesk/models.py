from django.db import models
class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='images/', default='default.png')



