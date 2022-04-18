from django.urls import path
from . import views 
from .views import AddLike,AddDislike,AddCommentDislike,UserRegisterView,AddCommentLike,likecomment,dislikecomment,ProfileList,ProfileDetail,PostList,PostDetails,CommentsList,CommentsDetails,TagList,TagsDetails
urlpatterns = [ 
    path('',views.home,name='home'),
    path("profile/", views.my_profile, name="profile"),
    path("profile/updateprofile/", views.update_profile_form, name="updateprofileform"),
    path("profile/update/", views.update_profile, name="updateprofile"),
    path('tags/', views.tags, name='tags'),
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
    path('post/dislikecomment/<int:id>/<int:ids>',dislikecomment,name='dislikecomment'),

    path("api/profile/",ProfileList.as_view(),name="profileApi"),
    path("api/profile/<int:pk>",ProfileDetail.as_view(),name="profiledetail"),
    path("api/post/",PostList.as_view(),name="postApi"),
    path("api/post/<int:pk>",PostDetails.as_view(),name="postdetail"),
    path("api/comments/",CommentsList.as_view(),name="commentsApi"),
    path("<int:pk>",CommentsDetails.as_view(),name="commentsdetail"),
    path("api/tags/",TagList.as_view(),name="tagApi"),
    path("<int:pk>",TagsDetails.as_view(),name="tagdetail"),
]


