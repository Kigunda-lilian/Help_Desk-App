# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# # Create your models here.

# class MyUserManager(BaseUserManager):
#     def create_user(self,email,user_name,contact,password=None):
#         if not email:
#             raise ValueError("email is required")
#         if not user_name:
#             raise ValueError("user name is required")
#         if not contact:
#             raise ValueError("please provide an active contact")
        
#         user=self.model(
#             email=self.normalize_email(email),
#             user_name=user_name,
#             contact=contact
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user


#     def create_superuser(self,email,user_name,contact,password=None):
#         user=self.create_user(
#             email=email,
#             user_name=user_name,
#             contact=contact,
#             password=password
#         )
#         user.is_admin=True
#         user.is_staff=True
#         user.is_superuser=True
#         user.save(using=self._db)
#         return user

# class MyUser(AbstractBaseUser):
#     email=models.EmailField(verbose_name="email address",max_length=60,unique=True)
#     user_name=models.CharField(verbose_name="user name",max_length=200,unique=True)
#     contact=models.CharField(max_length=20,verbose_name="personal contact")
#     date_posted=models.DateTimeField(verbose_name="date posted", auto_now_add=True)
#     last_login=models.DateTimeField(verbose_name="last login", auto_now=True)
#     is_admin=models.BooleanField(default=False)
#     is_staff=models.BooleanField(default=False)
#     is_active=models.BooleanField(default=True)
#     is_superuser=models.BooleanField(default=True)

#     USERNAME_FIELD="email"

#     REQUIRED_FIELDS=['user_name','contact']

#     objects=MyUserManager()

#     def __str__(self):
#         return self.user_name
    
#     def has_perm(self,perm,obj=None):
#         return True
    
#     def has_module_perms(self,app_label):
#         return True