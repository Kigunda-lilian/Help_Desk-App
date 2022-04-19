from rest_framework import serializers
from .models import Profile,Post,Tag,Comment
# profile serializer
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ( "user", "prof_pic ", "bio")
# post serializer
class  PostSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Post
        fields = ("id","post_owner","question","posted_on" )
# tag serializer
class  TagSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Tag
        fields = ("language","stage","title","description")
# comments serializer
class  CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("post", "user","body","date" )
