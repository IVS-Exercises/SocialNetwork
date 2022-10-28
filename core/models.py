from ast import Pass
from distutils.command.upload import upload
from email.mime import image
from enum import unique
import random
from platform import release
import profile
from pyexpat import model
from django.db import models

from django.contrib.auth.models import User
class frofiles(models.Model):
    NickName= models.CharField(max_length=100);
    description= models.CharField(max_length=1000);
    AvatarImage= models.ImageField(upload_to="avatar",default='default-avatar-profile.jpg');
    Followers= models.IntegerField();
    Followeing = models.IntegerField();
    user= models.OneToOneField(
        User,
        related_name='Frofiles', 
        blank=False , 
        unique = True,
        on_delete=models.CASCADE,
        )
    def __str__(self):
        return self.user.username
class follows(models.Model):
    profile= models.ForeignKey(frofiles,related_name='Follows', on_delete=models.CASCADE)
    user= models.ForeignKey(User, related_name='Follows', on_delete=models.CASCADE)
class posts(models.Model):
    Title = models.CharField(max_length=300,blank=False)
    Content =  models.TextField(blank=False)
    image =models.ImageField(upload_to="postImg")
    user = models.ForeignKey(User, related_name='posts',on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
class likes(models.Model):
    User = models.ForeignKey(User,related_name='Likes', on_delete=models.CASCADE),
    posts = models.ForeignKey(posts,related_name='Likes',on_delete=models.CASCADE)
class comments(models.Model):
    User = models.ForeignKey(User,related_name='Comments', on_delete=models.CASCADE),
    posts = models.ForeignKey(posts,related_name='Comments',on_delete=models.CASCADE)

