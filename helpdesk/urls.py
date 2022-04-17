from django.urls import path
from . import views
from.views import ProfileList,ProfileDetail,PostList,PostDetails,CommentsDetails,CommentsList,TagList,TagsDetails
from .views import AddLike,AddDislike
urlpatterns = [ 
    path('',views.home,name='home'),
    path("profile/", views.my_profile, name="profile"),
    path("profile/updateprofile/", views.update_profile_form, name="updateprofileform"),
    path("profile/update/", views.update_profile, name="updateprofile"),
    path("post/", views.post, name="post"),
    path('post/<int:pk>/like', AddLike.as_view(), name='like'),
    path('post/<int:pk>/dislike', AddDislike.as_view(), name='dislike'),
    path('details/<int:pk>/approve_ans', views.approve_ans, name='approve_ans'),
    path("add_question/", views.add_question, name="add_question"),
    path("questions/", views.questions, name="questions"),
    path("questions/<int:id>", views.details, name="details"),
    path('search/', views.search, name='search'),
    path('approve_ans/', views.approve_ans, name='approve_ans'),
    path("tags/",views.tags,name="tags"),
    
    #API
    path("api/profile/",ProfileList.as_view(),name="profileApi"),
    path("<int:pk>",ProfileDetail.as_view(),name="profiledetail"),
    path("api/post/",PostList.as_view(),name="postApi"),
    path("<int:pk>",PostDetails.as_view(),name="postdetail"),
    path("api/comments/",CommentsList.as_view(),name="commentsApi"),
    path("<int:pk>",CommentsDetails.as_view(),name="commentsdetail"),
    path("api/tags/",TagList.as_view(),name="tagApi"),
    path("<int:pk>",TagsDetails.as_view(),name="tagdetail"),
]


