from django.shortcuts import render, get_object_or_404
from . import models

def blogs(req):
    blogs = models.Blog.objects
    return render(req, 'blog/blogs.html', { 'blogs': blogs.all })

def detail(req, blog_id):
    detail_blog = get_object_or_404(models.Blog, pk=blog_id)
    return render(req, 'blog/detail.html', { 'blog': detail_blog  })
