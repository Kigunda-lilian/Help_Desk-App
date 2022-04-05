from django.shortcuts import render
# from django.conf import settings
# Create your views here.

# User = settings.AUTH_USER_MODEL
def tags(request):
    return render(request, 'questions/tags.html')
