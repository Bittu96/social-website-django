from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# def add_my_login_form(request):
#     if request.method == 'POST':
#         username = request.POST.get('login_username')
#         password = request.POST.get('login_password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             messages.success(
#                 request, 'you have successfully logged in!')
#         else:
#             messages.warning(
#                 request, 'username or password is invalid! Please try again..')
#     return {}#render(request, 'global/trending.html')