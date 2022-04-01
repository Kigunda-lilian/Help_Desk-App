from django.db import models
from authentication.models import Account
class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='images/', default='default.png')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    user = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='profile')



