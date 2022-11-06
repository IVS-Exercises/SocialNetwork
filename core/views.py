from asyncio.windows_events import NULL
from cProfile import Profile
from decimal import InvalidOperation
from email import message
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from itertools import chain
from django.db import models
from django.http import HttpResponse
import os

from core.models import Profiles

@login_required(login_url='signin')
def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        userName = request.POST['username']
        email = request.POST['email']
        passWord = request.POST['password']
        passWord2 = request.POST['password2']
        if passWord == passWord2:
            if User.objects.filter(username=userName).exists():
                messages.info(request, 'user already exists')
                return redirect('signup')

            if User.objects.filter(email=email).exists():
                messages.info(request, ''+email+' already exists')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=userName, email=email, password=passWord)
                user.save()
                ## setting account after create user and profile
                user_login=auth.authenticate(username=userName, password=passWord)
                auth.login(request,user_login)
                redirect('setting')

                ## create profile for the user
                user_model =  User.objects.get(username=userName)
                new_profile = Profiles.objects.create(user=user_model, user_id=user_model.id ,NickName=user_model.username)
                new_profile.save()

                ## move to setting page for profile after create new account
                return redirect('setting')
        else:
            messages.info(request, 'password don\'t same as comfirm password')
            return redirect('signup')
    return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user =auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, 'user or passworld not found')
            return redirect('signin')
    return render(request, 'signin.html')

def logout(request):
    auth.logout(request)
    return redirect('signin')

@login_required(login_url='signin')
def setting(request):
    print("into setting")
    user_profile = Profiles.objects.get(user=request.user)
    print("check method : "+request.method)
    if request.method == 'POST':
        print("method is POST")
        if request.FILES.get('image') == None:
            print("image is empty")
            image = user_profile.AvatarImage
            description = request.POST['description']
            print("description : "+  description)

            user_profile.AvatarImage = image
            user_profile.description = description
            user_profile.save()
        if request.FILES.get('image') != None:
            print("image is exists")
            image = request.FILES.get('image')
            description = request.POST['description']

            user_profile.AvatarImage = image
            user_profile.description = description

            user_profile.save()
        redirect('setting')
    return render(request,'setting.html',{'user_profile':user_profile})