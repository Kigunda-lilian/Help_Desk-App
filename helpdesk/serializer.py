from rest_framework import serializers
from .models import Profile,Post,Tag,Comments

# profile serializer
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("user", "prof_pic ", "bio")
        
class  PostSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Post
        fields = ("id","user","title","question","posted_on" )
        
class  TagSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Tag
        fields = ("language","stage","title","description") 
        
        
class  CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ("question", "user", "name","reply", "posted_on" ) 