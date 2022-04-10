from django.contrib import admin
from authentication.models import Account
from .models import Profile,Comments,Tag,Like,Post
admin.site.register(Comments)
admin.site.register(Profile)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Like)







