from django.db import models
from django.views.generic import ListView, DetailView
from .models import Article
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
class ArticleList(ListView):
    model = Article
    template_name = 'article_list.html'

class ArticleDetail(DetailView):
    model = Article
    template_name = 'article_detail.html'

class ArticleUpdate(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Article
    fields = ('title', 'summary', 'body', 'photo')
    template_name = 'article_edit.html'

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        if self.request.user.is_staff:
            return True
        
class ArticleDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        if self.request.user.is_staff:
            return True

class ArticleCreate(LoginRequiredMixin, CreateView):
    model = Article
    fields = ('title', 'summary', 'body', 'photo')
    template_name = 'article_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)