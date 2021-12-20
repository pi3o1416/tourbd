
from django.urls import path
from . import views

app_name='post'
urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('create-post/', views.CreatePost.as_view(), name='create_post')
]

