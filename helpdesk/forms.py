from django.forms import ModelForm
from django import forms
from . models import Post,Profile,Comments,Like

<<<<<<< HEAD

class PostForm(ModelForm):
    class Meta:
        model=Post
=======
from helpdesk.views import Post
from . models import Comments,Profile,Like,Post


class PostForm(ModelForm):
    class Meta:
        model=Comments
>>>>>>> 46f02dcd8b3401a94ef8676da8ed6fbc47913129
        fields="__all__"



class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    exclude = ['user']

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comments
    exclude = ['username', 'post']
    
class LikesForm(forms.Form):
  class Meta:
    model = Like
    exclude = '__all__'

class UpdateProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields=['prof_pic','bio']

class AddPostForm(forms.ModelForm):
  class Meta:
    model = Post
    exclude = []


