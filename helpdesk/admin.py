from django.contrib import admin

from .models import Profile,Comments,Tag,Like,Post

admin.site.register(Profile)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comments)


