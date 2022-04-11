from django.urls import path
from . import views
from.views import ProfileList,ProfileDetail,PostList,PostDetails,CommentsDetails,CommentsList,TagList,TagsDetails
urlpatterns = [ 
    path('',views.home,name='home'),
    path("profile/", views.my_profile, name="profile"),
    path("profile/updateprofile/", views.update_profile_form, name="updateprofileform"),
    path("profile/update/", views.update_profile, name="updateprofile"),
    path("add_question/", views.add_question, name="add_question"),
    path("questions/", views.questions, name="questions"),
    path("questions/<int:id>", views.details, name="details"),
    path('tags/', views.tags, name='tags'),
    
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


