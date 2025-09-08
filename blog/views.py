from django.shortcuts import render, get_object_or_404
from .models import BlogPost

def blog_list(request):
    # Get published posts, ordered by date (newest first)
    posts = BlogPost.objects.filter(is_published=True).order_by('-published_date')
    return render(request, 'blog/list.html', {'posts': posts})

def blog_detail(request, slug):
    # Get a single post or return 404
    post = get_object_or_404(BlogPost, slug=slug, is_published=True)
    return render(request, 'blog/detail.html', {'post': post})