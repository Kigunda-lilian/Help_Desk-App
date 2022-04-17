from django.urls import path
from . import views 
from .views import AddLike,AddDislike,AddCommentDislike,UserRegisterView,AddCommentLike,likecomment,dislikecomment
urlpatterns = [ 
    path('',views.home,name='home'),
    path("profile/", views.my_profile, name="profile"),
    path("profile/updateprofile/", views.update_profile_form, name="updateprofileform"),
    path("profile/update/", views.update_profile, name="updateprofile"),
    path("post/", views.post, name="post"),
    path('post/<int:pk>/like', AddLike.as_view(), name='like'),
    path('post/<int:pk>/dislike', AddDislike.as_view(), name='dislike'),
    path('post/<int:post_pk>/comment/<int:pk>/like', AddCommentLike.as_view(), name='comment-like'),
    path('post/<int:post_pk>/comment/<int:pk>/dislike', AddCommentDislike.as_view(), name='comment-dislike'),
    path('details/<int:pk>/approve_ans', views.approve_ans, name='approve_ans'),
    path("add_question/", views.add_question, name="add_question"),
    path("questions/", views.questions, name="questions"),
    path("questions/<int:id>", views.details, name="details"),
    path('search/', views.search, name='search'),
    path('approve_ans/<int:id>/', views.approve_ans, name='approve_ans'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('post/likecomment/<int:id>/<int:ids>',likecomment,name='likecomment'),
    path('post/dislikecomment/<int:id>/<int:ids>',dislikecomment,name='dislikecomment')



]

