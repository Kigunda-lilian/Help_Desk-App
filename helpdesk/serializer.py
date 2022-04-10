from rest_framework import serializers
from .models import Profile,Post

# profile serializer
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("user", "prof_pic ", "bio")
        
class  PostSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Post
        fields = ("id","user","title","question","posted_on" )