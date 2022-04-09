from django.contrib import admin
from authentication.models import Account
from .models import Profile
from helpdesk.models import Comments, Like, Post, Tag
admin.site.register(Account)
admin.site.register(Profile)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Like)








