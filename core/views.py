from decimal import InvalidOperation
from email import message
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.shortcuts import render, redirect
from django.db import models
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        userName = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=userName).exists():
                messages.info(request, 'user already exists')
                return redirect('signup')

            if User.objects.filter(email=email).exists():
                messages.info(request, ''+userName+' already exists')
                return redirect('signup')
            else:
                user = User.objects.create(
                    username=userName, email=email, password=password)
                user.save()
        else:
            messages.info(request, 'password don\'t same as password2')
            return redirect('signup')
    return render(request, 'signup.html')
