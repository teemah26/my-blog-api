from rest_framework import viewsets, permissions, filters
from .models import BlogPost, Comment
from .serializers import BlogPostSerializer, CommentSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

import django_filters
from django_filters import AllValuesFilter,DateTimeFilter,NumberFilter
from django_filters.rest_framework import DjangoFilterBackend
from django_filters.rest_framework import AllValuesFilter,DateTimeFilter,NumberFilter
from rest_framework import filters
from rest_framework import permissions

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class BlogPost(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['created_at', 'title']
    search_fields = ['title', 'content']
    name= 'blogpost'
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class Comment(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    name='comment'
    def perform_create(self, serializer):
        # You must include post in the request or set it here
        post_id = self.request.data.get('post')
        post = BlogPost.objects.get(id=post_id)
        serializer.save(commenter=self.request.user, post=post)
   


class ApiRoot(generics.GenericAPIView):
    name='api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'blog-post': reverse(BlogPost.name, request=request),
            'comment': reverse(Comment.name, request=request),
            
        })