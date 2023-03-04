from django.db import models

# Create your models here.


class SoundHomeUsers(models.Model):
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=254)


class SoundHomeUsersAdditionalInfo(models.Model):
    user = models.OneToOneField(
        SoundHomeUsers, on_delete=models.CASCADE, primary_key=True)

    image = models.ImageField("Auatar", upload_to="auatars/", null=True, blank=True)
    nickname = models.CharField(
        "Name", max_length=50, 
        blank=True, default="anonim", unique=True, null=True)
    active = models.BooleanField("Status", default=False)