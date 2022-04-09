from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('helpdesk.urls')),
    path('accounts/', include('django_registration.backends.activation.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
<<<<<<< HEAD
<<<<<<< HEAD


=======
>>>>>>> c0de2db792b184b7a83b3f55980be40b05d5ecc7
=======
>>>>>>> 46f02dcd8b3401a94ef8676da8ed6fbc47913129
]
