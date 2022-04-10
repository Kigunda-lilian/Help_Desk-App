from django.urls import path
from . import views
from.views import ProfileList,ProfileDetail,PostList,PostDetails
urlpatterns = [ 
    path('',views.home,name='home'),
    path("profile/", views.my_profile, name="profile"),
    path("api/profile/",ProfileList.as_view(),name="profileApi"),
    path("<int:pk>",ProfileDetail.as_view(),name="profiledetail"),
    path("api/post/",PostList.as_view(),name="profileApi"),
    path("<int:pk>",PostDetails.as_view(),name="profiledetail"),
    path("profile/updateprofile/", views.update_profile_form, name="updateprofileform"),
    path("profile/update/", views.update_profile, name="updateprofile"),
    path("add_question/", views.add_question, name="add_question"),
    path("questions/", views.questions, name="questions"),
    path("questions/<int:id>", views.details, name="details"),
    path('tags/', views.tags, name='tags')
]


