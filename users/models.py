from django.db import models

# Create your models here.


class SoundHomeUsers(models.Model):
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=254)


class SoundHomeUsersAdditionalInfo(models.Model):
    image = models.OneToOneField(
        SoundHomeUsers, on_delete=models.CASCADE, 
        primary_key=True, verbose_name="Autar")
    nickname = models.CharField(
        "Name", max_length=50, 
        blank=True, default="Anonim", unique=True)
