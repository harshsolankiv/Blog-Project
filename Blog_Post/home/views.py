import email
from django.shortcuts import render, HttpResponse
from matplotlib.pyplot import title
from .models import Contact
from blog.models import Post
from django.contrib import messages
# Create your views here.


def home(request):
    return render(request, "home/home.html")


def about(request):
    return render(request, "home/about.html")


def contact(request):

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        if (len(phone) < 10):
            messages.error(request, "phone number must be of 10 digits")
        else:
            contact = Contact(name=name, email=email,
                              phone=phone, content=desc)
            contact.save()
            messages.success(
                request, "Your Query has been sent successfuly!!!")
    return render(request, "home/contact.html")


def search(request):
    query = request.GET['query']
    if len(query)>78:
        allPosts = Post.objects.none()
    else:
        allPoststitle = Post.objects.filter(title__icontains=query)
        allPostContent = Post.objects.filter(content__icontains=query)
        allPosts = allPoststitle.union(allPostContent)
    
    if allPosts.count() ==0:
        messages.warning(request, "No search results found please refine your query")
        
    params = {'allPosts':allPosts,
              'query':query,
              }
    return render(request,'home/search.html',params)