
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post
from .forms import FilterForm, PostCreateForm


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


class AuthorDetail(View):
    def get(self, request):
        pass

    def post(self, request):
        pass


class PostDetail(View):
    template_name = 'post/post_detail.html'

    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        return render(request, self.template_name, {'post': post})

    def post(self, request):
        pass


class CreatePost(LoginRequiredMixin, View):
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

    def get(self):
        pass

    def post(self):
        pass


class EditPost(LoginRequiredMixin, View):
    template_name = 'post/edit_post.html'

    def get(self):
        pass

    def post(self):
        pass
