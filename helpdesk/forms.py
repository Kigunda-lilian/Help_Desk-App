from django.forms import ModelForm
from django import forms
from . models import Post,Profile,Comments,Like


class QuestionForm(ModelForm):
    class Meta:
        model=Post
        fields="__all__"



class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    exclude = ['user']

class CommentsForm(forms.ModelForm):
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

class AddQuestionForm(forms.ModelForm):
  class Meta:
    model = Post
    exclude = []


