from django.db import models

# Create your models here.


class SoundHomeUsers(models.Model):
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=254)
