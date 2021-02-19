from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from .models import Post, Tag
from .forms import CreatePostForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# import requests
# url = ('http://newsapi.org/v2/top-headlines?'
#        'sources=bbc-news&'
#        'apiKey=0d8f819341fd48f39c163d6102dc0240')
# response = requests.get(url)
# # print(response.json())

class PostListView(ListView):
    model = Post
    template_name = 'blog/blog_list.html'

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['posts'] = Post.objects.all()
            # context['news'] = response.json()
            return context

    # context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/blog_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/blog_form.html'
    fields = ['category', 'title', 'content', 'tags']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/blog_form.html'
    fields = ['category', 'title', 'content', 'tags']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


    def test_func(self):
        post = self.get_object()
        print("egeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",post)
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    # success_url = reverse('blog/')

    def get_success_url(self):
        return reverse('blog:blog_list')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
