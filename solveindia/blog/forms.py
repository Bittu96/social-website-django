from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post
from django import forms

class CreatePostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'title', 'content', 'author']
        widgets = {
            'content': forms.Textarea(attrs={'rows':4}),
        }
