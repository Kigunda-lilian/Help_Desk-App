from django.urls import path
from . import views
urlpatterns = [ 
    path('',views.home,name='home'),
    path("profile/", views.my_profile, name="profile"),
    path("profile/updateprofile/", views.update_profile_form, name="updateprofileform"),
    path("profile/update/", views.update_profile, name="updateprofile"),
    path("add_question/", views.add_question, name="add_question"),
    path("questions/", views.questions, name="questions"),
    path("questions/<int:id>", views.details, name="details"),
<<<<<<< HEAD
    path('tags/', views.tags, name='tags'),
=======
    path('tags/', views.tags, name='tags')
>>>>>>> 46f02dcd8b3401a94ef8676da8ed6fbc47913129
]


