
from django.urls import path
from . import views

app_name='post'
urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('create-post/', views.CreatePost.as_view(), name='create_post'),
    path('edit-post/<int:pk>/', views.EditPost.as_view(), name='edit_post'),
    path('delete-post/<int:pk>/', views.DeletePost.as_view(), name='delete_post'),
    path('delete_post/<int:pk>/complete/', views.DeletePostComplete.as_view(), name='delete_post_complete'),
    path('author/<str:username>/', views.AuthorPosts.as_view(), name='author_posts'),
]

