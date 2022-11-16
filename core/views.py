import os
from asyncio.windows_events import NULL
from cProfile import Profile
from decimal import InvalidOperation
from email import message
from itertools import chain
from django.core.exceptions import ObjectDoesNotExist

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.db import models
from django.http import HttpResponse
from django.shortcuts import redirect, render

from core.models import Follows, Likes, Posts, Profiles


@login_required(login_url='signin')
def index(request):
    user_object= User.objects.get(username=request.user.username)
    try:
        user_profile = Profiles.objects.get(user=user_object)
    except ObjectDoesNotExist:
        return render(request, 'signin.html')

    user_following_list = []
    feed = []

    user_following = Follows.objects.filter(user=request.user)

    for users in user_following:
        user_following_list.append(users.profile)
    for profile in user_following_list:
        feed_lists = Posts.objects.filter(user=profile.user)
        feed.append(feed_lists)
    post_user =Posts.objects.filter(user=user_object)
    feed.append(post_user)
    feed_list = list(chain(*feed))

    return render(request,'index.html',{'user_profile':user_profile ,
    'posts':feed_list,'all_profiles':Profiles.objects.all()})



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
        redirect('/')
    return render(request,'setting.html',{'user_profile':user_profile})

@login_required(login_url='signin')
def upload(request):
    if(request.method == 'POST'):
       user =   request.user
       image =  request.FILES.get('image_upload')
       caption = request.POST['caption']
       if image is None:
            messages.info(request, 'you need a image to upload')
            return redirect('/')
       new_post = Posts.objects.create(user=user, image=image, Content=caption)
       new_post.save()
       return redirect('/')
    else:
        return redirect('/')

@login_required(login_url='signin')
def like_post(request):
    user = request.user
    post_id = request.GET.get('post_id')

    post =  Posts.objects.get(id=post_id)
    like_filter = Likes.objects.filter(posts=post, user=user).first()
    if like_filter == None:
        new_like = Likes.objects.create(posts=post, user=user)
        new_like.save()
        post.no_of_likes = post.no_of_likes+1
        post.save()
        return redirect('/')
    else:
        like_filter.delete()
        post.no_of_likes = post.no_of_likes-1
        post.save()
        return redirect('/')

@login_required(login_url='signin')      
def delete(request):
    user = request.user
    post_id = request.GET.get('post_id')

    post =  Posts.objects.get(id=post_id)

    print(f"{user.id}, {post.user.id}")

    if user.id == post.user.id:
        post.delete()
        return redirect('/')
    else:
        redirect('/')

@login_required(login_url='signin')
def profile(request, pk):
    user_object = User.objects.get(username=pk)
    user_profile = Profiles.objects.get(user=user_object)
    user_posts = Posts.objects.filter(user=user_object)
    user_post_length = len(user_posts)
    user_followers =  len(Follows.objects.filter(profile=user_profile))
    user_following = len(Follows.objects.filter(user=user_object))

    user =  request.user
    check_followers = Follows.objects.filter(user=user,profile=user_profile).first()
    if check_followers is None:
        status = 'follow'
    else:
        status =  'Unfollow'

    print("status : "+status)
    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        'user_posts': user_posts,
        'user_post_length': user_post_length,
        'status': status,
        'user_followers': user_followers,
        'user_following': user_following
    }

    return render(request, 'profile.html', context)

@login_required(login_url='signin')
def follow(request):
    if request.method == 'POST':
        user_id =  request.POST['user_id']
        profile_id = request.POST['profile_id']
        username =  request.POST['username']

        profile =  Profiles.objects.get(id=profile_id)
        user = User.objects.get(id=user_id)
        print(user_id is None)
        print(profile_id is None)
        object_follower = Follows.objects.filter(profile=profile_id,user=user_id).first()
        if object_follower != None:
            delete_record =  Follows.objects.get(profile=profile_id,user=user_id)
            delete_record.delete()
            return redirect('/profile/'+username)
        else:
            new_follower = Follows.objects.create(profile=profile,user=user)
            new_follower.save()
            return redirect('/profile/'+username)
    else:
        return redirect('/')
