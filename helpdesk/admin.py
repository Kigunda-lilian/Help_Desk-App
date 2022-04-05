from re import A
from django.contrib import admin
<<<<<<< HEAD
# Register your models here
=======
from authentication.models import Account
<<<<<<< HEAD
from helpdesk.models import Comments, Like, Post, Tag
admin.site.register(Account)
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comments)
admin.site.register(Like)


=======
from .models import Profile
admin.site.register(Account)
admin.site.register(Profile)
>>>>>>> origin/development
>>>>>>> development
