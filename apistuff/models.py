from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class StuffAndTokens(models.Model):
    """ This model is storing stuff and those tech. api tokens """
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=300)
    duration_field = models.DurationField()
