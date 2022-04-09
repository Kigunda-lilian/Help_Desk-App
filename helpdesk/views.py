<<<<<<< HEAD

from django.shortcuts import render,redirect,get_object_or_404
from .models import Like, Post,Profile, Comments,Tag
=======
from django.shortcuts import render,redirect,get_object_or_404
from .models import Like, Post,Profile, Comments
>>>>>>> c0de2db792b184b7a83b3f55980be40b05d5ecc7
from helpdesk import views,forms
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
<<<<<<< HEAD
from .forms import LikesForm, CommentForm,PostForm
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Profile,Comments


=======
from .forms import LikesForm, CommentsForm,PostForm
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Profile,Comments
>>>>>>> c0de2db792b184b7a83b3f55980be40b05d5ecc7
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth import login, views, forms
from . import models




def home(request):
    return render(request, 'index.html', {})
    
def my_profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    context={'profile': profile}
    return render(request, 'profile.html', context)

@login_required(login_url='/accounts/login/')
def update_profile_form(request):

    context={}
    return render(request, 'Update_profile.html',context)

@login_required(login_url='/accounts/login/')
def update_profile(request):
    if request.method == "POST":
        current_user = request.user
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        bio = request.POST["bio"]
        name = request.POST["first_name"] + " " + request.POST["last_name"]

        profile_image = request.FILES["profile_pic"]
<<<<<<< HEAD
      
=======
>>>>>>> c0de2db792b184b7a83b3f55980be40b05d5ecc7
        profile_url = profile_image["url"]
        user = User.objects.get(id=current_user.id)
        if Profile.objects.filter(user_id=current_user.id).exists():

            profile = Profile.objects.get(user_id=current_user.id)
            profile.profile_pic = profile_url
            profile.save()
        else:
            profile = Profile(user_id=current_user.id,name=name,profile_pic=profile_url)

            profile.save_profile()

        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email
        user.bio=bio
        user.save()
        return redirect("/profile")
    else:
        return render(request, "Question_app/profile.html")

#display Questions
def questions(request):
    all_questions=models.Post.objects.all()
    return render(request,'all_questions.html', {'questions': all_questions})
#details
def details(request,id):
    obj=get_object_or_404(Post,pk=id)
    return render(request,'question-details.html', {'obj': obj})



<<<<<<< HEAD
def add_question(request):
=======
def post(request):
>>>>>>> c0de2db792b184b7a83b3f55980be40b05d5ecc7
    form=PostForm()
    if(request.method=='POST'):
        form_results=PostForm(request.POST)
        if form_results.is_valid():
            form_results.save()
            return redirect('/')
    context={'form':form}
    return render(request,'add_question.html',context)

 
def add_question(request): 

    if request.user.is_staff:
        form=PostForm()
        if(request.method=='POST'):
            form_results=PostForm(request.POST)
            if form_results.is_valid():
                form_results.save()
                return redirect('/')
        context={'form':form}
        return render(request,'add_question.html',context)
    else: 
        return redirect('home')

@login_required(login_url="/accounts/login/")
def search(request):
    questions = Comments.objects.all()
    if 'query' in request.GET and request.GET["query"]:
        search_term = request.GET.get("query")
        searched_results = Comments.objects.filter(question__icontains=search_term)
        message = f"Search For: {search_term}"
        context = {"message": message, "businesses": searched_results}
        return render(request, "Question_app/search.html", context)
    else:
        message = "You haven't searched for any term"
        context = {"message": message,'questions':questions}
        return render(request, "Question_app/search.html", context)



def likes(request,post_id):
  likesForm = LikesForm()
<<<<<<< HEAD
  #  CRUD     
=======
>>>>>>> c0de2db792b184b7a83b3f55980be40b05d5ecc7
  obj1=Like.objects.create(user=request.user,post=get_object_or_404(Post,pk=post_id),likes=1)
  obj1.save()
  print(obj1)
  return redirect('')

def comments(request,post_id):
  commentsForm = CommentForm()
  if request.method == 'POST':
    commentsForm = CommentForm(request.POST)
    if commentsForm.is_valid():
      form = commentsForm.save(commit=False)
      form.user=request.user
      form.post = get_object_or_404(Post,pk=post_id)
      form.save()
  
  return redirect('')
<<<<<<< HEAD

def tags(request):
    tag = Tag.objects.all()
    return render(request, 'questions/tags.html',{'tags':tag})
=======
>>>>>>> c0de2db792b184b7a83b3f55980be40b05d5ecc7
