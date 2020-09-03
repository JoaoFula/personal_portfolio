from django.shortcuts import render, get_object_or_404
from .models import blog_post

def all_blogs(request):
    blog_count = blog_post.objects.count()
    blogs = blog_post.objects.order_by('-date')[:5]
    return render(request, 'blog/all_blogs.html', {'blogs': blogs, 'blog_count':blog_count})

def detail(request, blog_id):
    blog = get_object_or_404(blog_post, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog})


