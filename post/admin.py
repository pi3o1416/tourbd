from django.contrib import admin
from .models import Post, Like, Comment

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'post_date', 'district')
    list_filter = ('title', 'author', 'post_date', 'district')

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('post', 'user')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_text', 'user', 'post')
