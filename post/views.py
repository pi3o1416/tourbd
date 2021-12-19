
from django.shortcuts import render
from django.views import View
from .models import Post


class PostList(View):
    template_name = 'post/post_list.html'
    def get(self, request):
        posts = Post.objects.all()
        return render(request, self.template_name, {'posts': posts})

    def post(self):
        pass


class PostDetail(View):
    template_name = 'post/post_detail.html'
    def get(self):
        pass

    def post(self):
        pass


class CreatePost(View):
    template_name = 'post/create_post.html'
    def get(self):
        pass

    def post(self):
        pass


class DeletePost(View):
    template_name = 'post/delete_post.html'
    def get(self):
        pass

    def post(self):
        pass


class EditPost(View):
    template_name = 'post/edit_post.html'
    def get(self):
        pass

    def post(self):
        pass

