import email
from django.shortcuts import render, HttpResponse
from .models import Contact
# Create your views here.


def home(request):
    return render(request, "home/home.html")


def about(request):
    return render(request, "home/about.html")


def contact(request):
    from django.contrib import messages
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
