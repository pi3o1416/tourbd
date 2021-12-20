
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post
from .forms import FilterForm, PostCreateForm
from .mixins import MyPermissionRequiredMixin


class PostList(View):
    form = FilterForm
    query_set = Post.objects.all().order_by('-post_date')
    template_name = 'post/post_list.html'

    def get(self, request):
        return render(request, self.template_name, {'posts': self.query_set, 'form': self.form()})

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if data['author']:
                self.query_set = self.query_set.filter(
                    author__username=data['author'])
            if data['date']:
                print(data['date'])
                print(type(data['date']))
                self.query_set = self.query_set.filter(post_date__year=data['date'].year,
                                                       post_date__month=data['date'].month,
                                                       post_date__day=data['date'].day)
            if data['title']:
                self.query_set = self.query_set.filter(
                    title__icontains=data['title'])
            if data['district']:
                self.query_set = self.query_set.filter(
                    district=data['district'])
            return render(request, self.template_name, {'posts': self.query_set, 'form': form})
        else:
            return render(request, self.template_name, {'posts': self.query_set, 'form': form})


class AuthorPosts(View):
    template_name = 'post/author_posts.html'
    author_model = get_user_model()
    def get(self, request, username):
        try:
            user = self.author_model.objects.get(username=username)
            query_set = Post.objects.filter(author__username = username)
            return render(request, self.template_name, {'posts': query_set, 'author': user})
        except self.author_model.DoesNotExist:
            return render(request, 'does_not_exist.html')


class PostDetail(View):
    template_name = 'post/post_detail.html'

    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        return render(request, self.template_name, {'post': post})

    def post(self, request):
        pass

class CreatePost(LoginRequiredMixin, MyPermissionRequiredMixin, View):
    permission_required = ('post.add_post',)
    template_name = 'post/create_post.html'
    form = PostCreateForm

    def get(self, request):
        form = self.form()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('post:post_list'))
        else:
            return render(request, self.template_name, {'form': form})


class DeletePost(LoginRequiredMixin, View):
    template_name = 'post/delete_post.html'

    def get(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
            return render(request, self.template_name, {'post': post})
        except Post.DoesNotExist:
            return render(request, 'does_not_exist.html')


class DeletePostComplete(LoginRequiredMixin, View):
    def get(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
            post.delete()
            return HttpResponseRedirect(reverse('post:author_posts', kwargs={'username': post.author.username}))
        except Post.DoesNotExist:
            return render(request, 'does_not_exist.html')


class EditPost(LoginRequiredMixin, View):
    form = PostCreateForm
    template_name = 'post/edit_post.html'

    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        form = self.form(instance=post)
        return render(request, self.template_name, {'form': form, 'post': post})

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        form = self.form(instance=post, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('post:post_detail', kwargs={'pk': post.pk}))
        else:
            return render(request, self.template_name, {'form': form, 'post': post})
