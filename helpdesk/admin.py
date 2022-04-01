from re import A
from django.contrib import admin
from authentication.models import Account
from .models import Profile
admin.site.register(Account)
admin.site.register(Profile)
