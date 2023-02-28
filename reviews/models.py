from django.db import models

# Create your models here.

class Review(models.Model):
    album_title = models.CharField(max_length=50)
    album_author = models.CharField(max_length=50)
    album_year = models.CharField(max_length=4)
    
    image_src = models.TextField(max_length=500)
    album_score = models.CharField(max_length=4)

    review_title = models.TextField(max_length=500)
    review_text = models.TextField(max_length=10_000)
