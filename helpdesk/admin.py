from django.contrib import admin
from authentication.models import Account
<<<<<<< HEAD
from .models import Profile
from helpdesk.models import Comments, Like, Post, Tag
admin.site.register(Account)
=======
from .models import Profile,Comments,Tag,Like,Post
admin.site.register(Comments)
>>>>>>> 46f02dcd8b3401a94ef8676da8ed6fbc47913129
admin.site.register(Profile)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Like)





<<<<<<< HEAD

=======
>>>>>>> 46f02dcd8b3401a94ef8676da8ed6fbc47913129


