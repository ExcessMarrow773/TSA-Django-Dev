# blog/models.py

from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.conf import settings
from django.utils import timezone
import datetime

class Category(models.Model):
    name = models.CharField(max_length=60)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.CharField(max_length=100, default='admin')
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    def was_published_recently(self):
            return self.created_on >= timezone.now() - datetime.timedelta(days=1)
    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    def __str__(self):
         return self.author