from django.shortcuts import render, HttpResponse
from matplotlib.style import context
from blog.models import Post
# Create your views here.


def blogHome(request):
    allPosts = Post.objects.all()
    context={
        'allPosts':allPosts,
    }
    return render(request, "blog/blogHome.html",context)


def blogPost(request, slug):
    post = Post.objects.filter(slug=slug)[0]
    context={
        'post':post,
    }
    return render(request, "blog/blogPost.html",context)
