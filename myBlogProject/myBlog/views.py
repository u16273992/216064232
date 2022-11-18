from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category,Comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

class AddCategoryView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

class AddCommentView(CreateView):
    model = Comment
    form_class =  CommentForm
    template_name = 'add_comment.html'
    success_url= reverse_lazy('home')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url= reverse_lazy('home')

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category = cats.replace('-',' '))
    return render(request, 'categories.html', {'cats':cats.title().replace('-',' '), 'category_posts':category_posts})