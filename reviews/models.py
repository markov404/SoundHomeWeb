from django.db import models

# Create your models here.

class Review(models.Model):
    album_title = models.CharField("Album title", max_length=50)
    album_author = models.CharField("Album author", max_length=50)
    album_year = models.CharField("Year of review", max_length=4)
    
    image_src = models.TextField("Album Image Src", max_length=500)
    album_score = models.CharField("Album Score", max_length=4)

    review_title = models.TextField("Review Title", max_length=500)
    review_text = models.TextField("Review Text", max_length=10_000)

    active = models.BooleanField("Status", default=False)

class ReviewTranslation(models.Model):
    review = models.OneToOneField(Review, on_delete=models.CASCADE, primary_key=True)
    translated_review_text = models.TextField("Translation", max_length=20_000, null=True, blank=True)

class ReviewAudio(models.Model):
    review = models.OneToOneField(Review, on_delete=models.CASCADE, primary_key=True)
    audio_review = models.FileField("Audio Review", upload_to='audio_reviews', null=True, blank=True)
