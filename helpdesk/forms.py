from django.forms import ModelForm
from django import forms
from . models import Post,Profile,Comment,Like


class PostForm(ModelForm):
    class Meta:
        model=Post
        fields="__all__"
        widgets = {
      'title': forms.TextInput(attrs={'class':'form-control'}),
      'question': forms.Textarea(attrs={'class':'form-control'}),
    }



class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    exclude = ['user']

class CommentForm(forms.ModelForm):
  body = forms.CharField(widget=forms.Textarea(attrs={'rows':4,
  }))
  class Meta:
    model = Comment
    fields = ['body']
    
    
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


