
# from blog.models import Post, Category
from django.shortcuts import get_object_or_404, render

from shelbycodes.blog.models import Post, Category


def index(request):
    return render(request, 'blog/index.html', {
        'categories': Category.objects.all(),
        'posts': Post.objects.all(),
    })


def view_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post.html', {
        'categories': Category.objects.all(),
        'posts': Post.objects.filter(category=post.category),
        'post': post,
    })


def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    print("cat:", slug)
    return render(request, 'blog/category.html', {
        'category': category,
        'categories': Category.objects.all(),
        'posts': Post.objects.filter(category=category)
    })


def view_projects(request):
    return render(request, 'blog/projects.html', {
        'categories': Category.objects.all(),
        'posts': Post.objects.all(),
    })


def blog_main(request):
    return render(request, 'blog/blog_main.html', {
        'categories': Category.objects.all(),
        'posts': Post.objects.all(),
    })


def about(request):
    return render(request, 'blog/about.html', {
        'categories': Category.objects.all(),
        'posts': Post.objects.all(),
    })
