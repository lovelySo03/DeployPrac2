from rest_framework import serializers
from .models import Article, Comment
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'name','nickname')
        
        
class ArticleListSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model = Article
        fields = ('id', 'title', 'content','user')




class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article','user')
        
        
class ArticleSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
