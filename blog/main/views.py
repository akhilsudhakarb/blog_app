from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from .models import Blogs, Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import BlogForm, EditForm


def blog_by_cat(request, cats):
    blogs = Blogs.objects.filter(category__name=cats)
    cat = Category.objects.all()
    return render(request, 'blog_by_category.html', {'blogs': blogs, 'cat': cat})



class HomeView(ListView):
    model = Blogs
    template_name = 'index.html'
    ordering = ['-date']

    def get_context_data(self, *args, **kwargs):
            cat = Category.objects.all()
            context = super(HomeView, self).get_context_data(*args, **kwargs)
            context['cat'] = cat
            return context


class ArticleDetailView(DetailView):
    model = Blogs
    template_name = 'article_details.html'


class AddArticleView(CreateView):
    model = Blogs
    form_class = BlogForm
    template_name = 'add_article.html'
    # fields = '__all__'



class UpdateArticleView(UpdateView):
    model = Blogs
    form_class = EditForm
    template_name = 'update_article.html'
    # fields = ['title', 'content']


class DeleteArticleView(DeleteView):
    model = Blogs
    template_name = 'delete_article.html'
    success_url = reverse_lazy('home')
    # fields = ['title', 'content']