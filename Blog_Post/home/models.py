from telnetlib import Telnet
from unicodedata import name
from django.db import models

# Create your models here.


class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    content = models.TextField()
    timestamp = models.DateField(auto_now_add=True, blank=True)

    def __str__(self):
        return "Message From: "+self.name
