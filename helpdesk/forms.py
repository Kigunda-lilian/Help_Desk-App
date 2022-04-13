from django.forms import ModelForm
from django import forms
from . models import Post,Profile,Comment,Like
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User


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

  class Meta:
    model = Comment
    fields = ('body',)
    widgets = {
      'body': forms.Textarea(attrs={'class':'form-control'}),
    }
    
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

#usr reg
class SignUpForm(UserCreationForm):
    email =forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name =forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name =forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')
    def __init__(self,  *args, **kwargs):
        super(SignUpForm,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['class']='form-control'
