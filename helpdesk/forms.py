from django.forms import ModelForm
from django import forms

from helpdesk.views import add_question
from . models import QuestionAnswer,Profile,Comment,Like,add_question


class QuestionForm(ModelForm):
    class Meta:
        model=QuestionAnswer
        fields="__all__"



class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    exclude = ['user']

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
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
    model = add_question
    exclude = []


