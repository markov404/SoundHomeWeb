from django.db import models
from django.apps import apps

from users.components.validators import (
    UserNicknameValidator, 
    UserAvaValidator,
    UserEmailValidator,
    UserPasswordValidator)

# Create your models here.


class SoundHomeUsers(models.Model):
    email = models.EmailField(
        max_length=254, 
        unique=True, 
        validators=[UserEmailValidator().is_valid])
    password = models.CharField(
        max_length=254,
        validators=[UserPasswordValidator().is_valid])


class SoundHomeUsersAdditionalInfo(models.Model):
    user = models.OneToOneField(
        SoundHomeUsers, on_delete=models.CASCADE, primary_key=True)

    image = models.ImageField(
        "Auatar", 
        upload_to="auatars/", 
        null=True, 
        blank=True,
        validators=[UserAvaValidator().is_valid])
    nickname = models.CharField(
        "Name", 
        max_length=50, 
        blank=True, 
        default="anonim", 
        unique=True, 
        null=True,
        validators=[UserNicknameValidator().is_valid])
    active = models.BooleanField("Status", default=False)


class SoundHomeUsersWhatUsersLikes(models.Model):
    user = models.ForeignKey('users.SoundHomeUsers', on_delete=models.CASCADE)
    user_review = models.ForeignKey('reviews.UserReview', on_delete=models.CASCADE)
      
    class Meta:
        unique_together = ('user', 'user_review',)
