from turtle import pos
from django.contrib import messages
from django.shortcuts import redirect, render, HttpResponse
from matplotlib.style import context
from blog.models import Post, BlogComment
from blog.templatetags import extras
# Create your views here.


def blogCreate(request):
    from datetime import datetime
# get time now
    dt = datetime.now()
# format it to a string
    timeStamp = dt.strftime('%Y-%m-%d %H:%M')
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['myhtml1']
        author = request.user.first_name + " " + request.user.last_name
        t = request.POST['title'].replace(" ", "-")
        slug = t+"-"+request.user.username
        timestamp = timeStamp

        post = Post(title=title, author=author, content=content,
                    slug=slug, timestamp=timestamp)
        post.save()
        messages.success(request, "Your Blog Posted Successfully 👏👏")

    return render(request, "blog/blogCreate.html")


def blogEdit(request):
    uname = request.user.first_name + " " + request.user.last_name
    pt = Post.objects.filter(author=uname)
    context = {
        'pt': pt
    }
    return render(request, "blog/blogEdit.html", context)


def blogHome(request):
    allPosts = Post.objects.all()
    context = {
        'allPosts': allPosts,
    }
    return render(request, "blog/blogHome.html", context)


def blogPost(request, slug):
    post = Post.objects.filter(slug=slug)[0]
    post.views = post.views+1
    post.save()
    comments = BlogComment.objects.filter(post=post, parent=None)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    context = {
        'post': post,
        'comments': comments,
        'user': request.user,
        'replyDict': replyDict,
    }
    return render(request, "blog/blogPost.html", context)


def postComment(request):
    if request.method == 'POST':
        comment = request.POST.get("comment")
        user = request.user
        postSno = request.POST.get("postSno")
        post = Post.objects.get(sno=postSno)
        parentSno = request.POST.get("parentSno")
        if parentSno == "":
            comment = BlogComment(comment=comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment posted 👏👏")
        else:
            parent = BlogComment.objects.get(sno=parentSno)
            comment = BlogComment(
                comment=comment, user=user, post=post, parent=parent)
        comment.save()
        messages.success(request, "Your reply posted 👏👏")

    return redirect(f"/blog/{post.slug}")


def delete(request, sno):
    item = Post.objects.get(sno=sno)
    item.delete()
    messages.success(request, ("Blog has been deleted!"))
    return redirect(blogEdit)


def Edit(request, sno):
    item2 = Post.objects.get(sno=sno)
    title2 = item2.title
    content2 = item2.content

    if request.method == 'POST':
        item2.title = request.POST['title']
        item2.content = request.POST['myhtml1']
        item2.save()
        messages.success(request, ("Blog has been Updated!"))
        return redirect(blogEdit)

    context = {
        'title2': title2,
        'content2': content2,
    }
    return render(request, "blog/edit.html/", context)
