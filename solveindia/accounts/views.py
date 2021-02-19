from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm, UpdateUserForm, ProfileUpdateForm
from .models import Profile
from blog.models import Post, Tag
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


import random
from accounts.models import Profile


# import requests
# # url = ('http://newsapi.org/v2/top-headlines?'
# #        'sources=bbc-news&'
# #        'apiKey=0d8f819341fd48f39c163d6102dc0240')

# url = ('http://newsapi.org/v2/top-headlines?'
#        'country=us&'
#        'apiKey=0d8f819341fd48f39c163d6102dc0240')

# response = requests.get(url)
# news = response.json()
# print(response.json())

def home(request):
    rand_range = range(1, 3000)
    user_data = Profile.objects.all()
    post_data = Post.objects.all()
    context = {'user_data': user_data,
               'rand_range': rand_range, 'posts': post_data}
    return render(request, 'home.html', context)


def feed(request):
    return render(request, 'global/feed.html')


@login_required
def profile(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'accounts/profile.html', context)


@login_required
def vprofile(request, username):
    try:
        vuser = User.objects.get(username=username)
    except:
        return render(request, 'accounts/profile.html')
    if request.user == vuser:
        return render(request, 'accounts/profile.html')
    context = {'vuser': vuser, 'posts': Post.objects.all()}
    return render(request, 'accounts/vprofile.html', context)


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('login_username')
        password = request.POST.get('login_password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            messages.success(
                request, 'you have successfully logged in! You can update your account anytime in your edit profile section!')
            return redirect('accounts:profile')
        else:
            messages.warning(
                request, 'username or password is invalid! Please try again..')

    context = {}
    return render(request, 'accounts/login.html', context)


def signup(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request, 'you have successfully created an account! Please login..')
            return redirect('accounts:login')

    context = {'form': form}
    return render(request, 'accounts/signup.html', context)


def accountPage(request):
    if request.method == 'POST':
        u_form = UpdateUserForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            p_form.save()
            u_form.save()

            messages.success(
                request, 'you have successfully updated your account!')
            return redirect('accounts:profile')
        else:
            messages.warning(
                request, 'Please check your data')

    else:
        u_form = UpdateUserForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {'u_form': u_form, 'p_form': p_form}
    return render(request, 'accounts/account.html', context)


def logoutUser(request):
    logout(request)
    messages.info(
        request, 'you have successfully logged out!')
    return redirect('home')
    # return redirect('accounts:login')


# @staff_member_required
def delete_user(request):
    username = request.user.username
    print(username)
    try:
        u = User.objects.get(username=username)
        u.delete()
        messages.success(request, "The user is deleted")
        return render(request, 'accounts/profile.html')

    except User.DoesNotExist:
        messages.error(request, "User doesnot exist")
        return render(request, 'accounts/account.html')

    finally:
        return render(request, 'accounts/account.html')

    return render(request, 'accounts/account.html')


def testforms(request):
    rand_range = range(1, 30)
    user_data = Profile.objects.all()
    post_data = Post.objects.all()
    context = {'user_data': user_data,
               'rand_range': rand_range, 'posts': post_data, }

    return render(request, 'global/testforms.html', context)


def user_search(request, *args, **kwargs):
    context = {}
    q_accounts = []
    q_blogs = []
    if request.method == "GET":
        search_query = request.GET.get("q")
        if len(search_query) > 0:
            search_results_accounts = User.objects.filter(username__icontains=search_query).distinct()
            search_results_blogs = Post.objects.filter(title__icontains=search_query).distinct()
            # user = request.user
              # [(account1, True), (account2, False)]
            for q_account in search_results_accounts:
                    q_accounts.append(q_account)
            for q_blog in search_results_blogs:
                    q_blogs.append(q_blog)
    context['q_accounts'] = q_accounts
    context['q_blogs'] = q_blogs

    return render(request, 'global/testforms.html', context)
