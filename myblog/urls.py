
from django.urls import path, include
from myblog import views


urlpatterns = [
    path('blog/',views.BlogPost.as_view(),name=views.BlogPost.name),
    path('comment/',views.Comment.as_view(),name=views.Comment.name)
]
