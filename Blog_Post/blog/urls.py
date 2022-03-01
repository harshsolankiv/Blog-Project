from django import views
from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('postComment', views.postComment, name="postComment"),
    path('blogCreate', views.blogCreate, name="blogCreate"),
    path('Edit/<sno>', views.Edit, name="Edit"),
    path('blogEdit', views.blogEdit, name="blogEdit"),
    path('', views.blogHome, name="blogHome"),
    path('<str:slug>', views.blogPost, name="blogPost"),
    path('delete/<sno>', views.delete, name="delete"),

]
