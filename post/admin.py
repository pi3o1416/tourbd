from django.contrib import admin
from .models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'post_date', 'district')
    list_filter = ('title', 'author', 'post_date', 'district')
