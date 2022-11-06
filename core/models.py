from ast import Pass
import datetime
from distutils.command.upload import upload
from email.mime import image
from email.policy import default
from enum import unique
import random
from platform import release
import profile
from pyexpat import model
from time import time
from django.db import models
from django.contrib.auth.models import User

class Profiles(models.Model):
    NickName= models.CharField(max_length=100);
    description= models.CharField(max_length=1000,blank=True);
    AvatarImage= models.ImageField(upload_to="avatar",default='default-avatar-profile.jpg');
    Followers= models.IntegerField(default=0);
    Followeing = models.IntegerField(default=0);
    user= models.OneToOneField(
        User,
        related_name='Frofiles', 
        blank=False , 
        unique = True,
        on_delete=models.CASCADE,
        )
    def __str__(self):
        return self.user.username
class Follows(models.Model):
    profile= models.ForeignKey(Profiles,related_name='Follows', on_delete=models.CASCADE)
    user= models.ForeignKey(User, related_name='Follows', on_delete=models.CASCADE)

class Posts(models.Model):
    Title = models.CharField(max_length=300,blank=False)
    Content =  models.TextField(blank=False)
    image =models.ImageField(upload_to="postImg")
    user = models.ForeignKey(User, related_name='posts',on_delete=models.CASCADE)
    no_of_likes= models.IntegerField(default=0)
    def __str__(self):
        return self.user.username

class Likes(models.Model):
    posts = models.ForeignKey(Posts,related_name='Likes',on_delete=models.CASCADE)
    user= models.ForeignKey(User,related_name='Likes', on_delete=models.CASCADE)
    
class Comments(models.Model):
    content = models.CharField(max_length=300, blank=False)
    dataTime = models.DateTimeField(default=datetime.datetime.now())
    posts = models.ForeignKey(Posts,related_name='Comments',on_delete=models.CASCADE)
    user= models.ForeignKey(User,related_name='Comments', on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
