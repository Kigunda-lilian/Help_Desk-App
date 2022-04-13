from multiprocessing import context
from django.shortcuts import render,redirect,get_object_or_404
from .models import Like, Post,Profile, Comment
from helpdesk import views,forms
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import LikesForm, CommentForm,PostForm
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.views import generic
from django.contrib.auth import login, views, forms
from . import models
from django.utils.text import slugify
from django.contrib import messages


from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views import View
from django.contrib.auth.forms import UserCreationForm

from django.urls import reverse_lazy
from .forms import SignUpForm


#search results
def search(request):
    if 'q' in request.GET:
        searched = request.GET['q']
        data = Post.objects.filter(title__icontains=searched)
    else:
        data = Post.objects.all()
    context = {
        'data': data
    }
    
    return render(request,'search.html', context)
    


#answers approval
def approve_ans(request):
    answers_list = Comment.objects.all().order_by('-id')
    if request.user.is_superuser:
        return render(request, 'approve_ans.html',{'answers_list': answers_list})

    else:
        messages.success(request,("You are not authorized to approve answers!"))
        return redirect('home')
    
    return render(request, 'approve_ans.html')



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
    if 'q' in request.GET:
        q = request.GET['q']
        all_questions = Post.objects.filter(question__icontains=q)
    else:
        all_questions=Post.objects.all()
    context = {
        'questions': all_questions
    }
    return render(request,'all_questions.html', context)
#details
def details(request,id):
    post=get_object_or_404(Post,pk=id)
    comments = Comment.objects.filter(post=post).order_by('-id')
    comment_form = CommentForm
    if request.method == 'POST':
        
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            body = request.POST.get('body')
            comment = Comment.objects.create(post=post, user=request.user, body=body)
            comment.save()
            return HttpResponseRedirect(post.get_absolute_url())
        else:
            comment_form= CommentForm()

    context = {
        'post': post,
        'comments':comments,
        'comment_form': comment_form,
    }
    
   
    return render(request, 'question-details.html', context)

def post(request):
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
    questions = Comment.objects.all()
    if 'query' in request.GET and request.GET["query"]:
        search_term = request.GET.get("query")
        searched_results = Comment.objects.filter(question__icontains=search_term)
        message = f"Search For: {search_term}"
        context = {"message": message, "businesses": searched_results}
        return render(request, "Question_app/search.html", context)
    else:
        message = "You haven't searched for any term"
        context = {"message": message,'questions':questions}
        return render(request, "search.html", context)


#likes for post
def likes(request,post_id):
  likesForm = LikesForm()
  obj1=Like.objects.create(user=request.user,post=get_object_or_404(Post,pk=post_id),likes=1)
  obj1.save()
  print(obj1)
  return redirect('')

#dislikes for post
class AddLike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)

        is_dislike = False

        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if is_dislike:
            post.dislikes.remove(request.user)

        is_like = False

        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break

        if not is_like:
            post.likes.add(request.user)

        if is_like:
            post.likes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)
#adddislikes for post
class AddDislike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)

        is_like = False

        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break

        if is_like:
            post.likes.remove(request.user)

        is_dislike = False

        for dislike in post.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if not is_dislike:
            post.dislikes.add(request.user)

        if is_dislike:
            post.dislikes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)

#comment likes and dislikes
def likes(request,post_id):
  likesForm = LikesForm()
  obj1=Like.objects.create(user=request.user,post=get_object_or_404(Post,pk=post_id),likes=1)
  obj1.save()
  print(obj1)
  return redirect('')

#dislikes for post
class AddCommentLike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        comment = Comment.objects.get(pk=pk)

        is_dislike = False

        for dislike in comment.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if is_dislike:
            comment.dislikes.remove(request.user)

        is_like = False

        for like in comment.likes.all():
            if like == request.user:
                is_like = True
                break

        if not is_like:
            comment.likes.add(request.user)

        if is_like:
            comment.likes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)
#adddislikes for post
class AddCommentDislike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        comment = Comment.objects.get(pk=pk)

        is_like = False

        for like in comment.likes.all():
            if like == request.user:
                is_like = True
                break

        if is_like:
            comment.likes.remove(request.user)

        is_dislike = False

        for dislike in comment.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if not is_dislike:
            comment.dislikes.add(request.user)

        if is_dislike:
            comment.dislikes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)


#user reg
class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'django_registration/registration_form.html'
    success_url = reverse_lazy('login')
    
