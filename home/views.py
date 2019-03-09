from django.shortcuts import render, redirect
from django.contrib.auth import logout


def home(request):
    return render(request, 'home.html')


def my_logout(request):
    # request.user.logout()
    logout(request)
    return redirect('home')
