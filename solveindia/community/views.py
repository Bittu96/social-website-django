from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import *

def community(request):
    context = {}
    return render(request, 'community/community.html', context)
