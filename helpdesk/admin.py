from django.contrib import admin
from .models import Profile,Comment,Tag,Like,Post,Dislike
admin.site.register(Profile)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Dislike)



