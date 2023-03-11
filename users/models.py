from django.db import models
from django.apps import apps

from users.components.validators import (
    UserNicknameValidator, 
    UserAvaValidator,
    UserEmailValidator,
    UserPasswordValidator)

# Create your models here.


class SoundHomeUsers(models.Model):
    """
    Stores basic user data.
    """
    email = models.EmailField(
        max_length=254, 
        unique=True, 
        validators=[UserEmailValidator().is_valid])
    password = models.CharField(
        max_length=254,
        validators=[UserPasswordValidator().is_valid])

    def __str__(self) -> str:
        return f'Email: {self.email} | Nickname: {self.soundhomeusersadditionalinfo.active}'


class SoundHomeUsersAdditionalInfo(models.Model):
    """
    Extend model 'users.SoundHomeUsers', related to it with
    one to one relationship.
    """
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

    def __str__(self) -> str:
        return f'Email: {self.user.email} | Active: {self.nickname}'


class SoundHomeUsersWhatUsersLikes(models.Model):
    """
    Stores relation between users and user_review that them likes
    related to 'users.SoundHomeUsers', and to 'reviews.UserReview', using
    many to one relationship. File 'user' and 'user_review' are unique-together.
    """

    user = models.ForeignKey('users.SoundHomeUsers', on_delete=models.CASCADE)
    user_review = models.ForeignKey('reviews.UserReview', on_delete=models.CASCADE)
      
    class Meta:
        unique_together = ('user', 'user_review',)

    def __str__(self) -> str:
        return f'User: {self.user.pk} | Review: {self.user_review.pk}'
