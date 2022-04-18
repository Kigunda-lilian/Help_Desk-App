from multiprocessing import context
from ssl import create_default_context
from django.shortcuts import render,redirect,get_object_or_404
from .models import Like, Post,Profile, Comment,Dislike, Tag
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
    #tags views
def tags(request):
    tag = Tag.objects.all()
    return render(request, 'questions/tags.html',{'tags':tag})
    


#answers approval
@login_required(login_url='/accounts/login/')
def approve_ans(request,id):
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
@login_required(login_url='/accounts/login/')
def post(request):
    form=PostForm()
    if(request.method=='POST'):
        form_results=PostForm(request.POST)
        if form_results.is_valid():
            form_results.save()
            return redirect('/')
    context={'form':form}
    return render(request,'add_question.html',context)

@login_required(login_url='/accounts/login/')
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
                is_like = Trueis_dislike = False
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




#likes for comment
class AddCommentLike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        comments = Comment.objects.get(pk=pk)

        is_dislike = False

        for dislike in comments.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if is_dislike:
            comments.dislikes.remove(request.user)

        is_like = False

        for like in comments.likes:
            if like == request.user:
                is_like = Trueis_dislike = False
                break

        if not is_like:
            comments.likes.add(request.user)
        

        if is_like:
            comments.likes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)


#adddislikes for comment
class AddCommentDislike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        comments = Comment.objects.get(pk=pk)

        is_like = False

        for like in comments.likes:
            if like == request.user:
                is_like = True
                break

        if is_like:
            comments.likes.remove(request.user)

        is_dislike = False

        for dislike in comments.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if not is_dislike:
            comments.dislikes.add(request.user)

        if is_dislike:
            comments.dislikes.remove(request.user)

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)
#user reg
class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'django_registration/registration_form.html'
    success_url = reverse_lazy('login')

@login_required(login_url='/accounts/login/')
def likecomment(request,id,ids):
    comment=Comment.objects.get(id=id)
    try:
        users=Dislike.objects.get(user=request.user,comment=comment)
        response='/questions/'+str(ids)
        return redirect(response)
    except:
        
        user=request.user
        check_like=Like.objects.filter(user=user)
        if check_like.exists():
            check_like=Like.objects.get(user=user)
            check_like.delete()
            comment.total_likes=comment.total_likes - 1
            comment.save()
        else:
            new_like=Like(user=user, response='like',comment=comment)
            new_like.save()
            comment.total_likes=comment.total_likes + 1
            comment.save()
        response='/questions/'+str(ids)
        return redirect(response)
@login_required(login_url='/accounts/login/')
def dislikecomment(request,id,ids):
    comment=Comment.objects.get(id=id)

    try:
        users=Like.objects.get(user=request.user,comment=comment)
        response='/questions/'+str(ids)
        return redirect(response)
    except:
        user=request.user
        check_like=Dislike.objects.filter(user=user)
        if check_like.exists():
            check_like=Dislike.objects.get(user=user)
            check_like.delete()
            comment.total_dislikes=comment.total_dislikes - 1
            comment.save()
        else:
            new_dislike=Dislike(user=user, response='dislike',comment=comment)
            new_dislike.save()
            comment.total_dislikes=comment.total_dislikes + 1
            comment.save()
        response='/questions/'+str(ids)
        return redirect(response)
    

    
