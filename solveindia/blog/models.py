from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import render, redirect

class Tag(models.Model):
    name = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100, null=True)
    content = models.TextField()
    date_posted = models.DateTimeField(
        default=timezone.now)  # auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('blog:blog_detail', kwargs={'pk': self.pk})