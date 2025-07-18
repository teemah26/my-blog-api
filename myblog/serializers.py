from rest_framework import serializers
from .models import BlogPost, Comment
from django.contrib.auth.models import User

class CommentSerializer(serializers.ModelSerializer):
    commenter = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'commenter', 'text', 'created_at')

class BlogPostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = BlogPost
        fields = ('id', 'author', 'title', 'content', 'created_at', 'comments')
