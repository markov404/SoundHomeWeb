import os

from django.dispatch import receiver
from django.db import models

from reviews.models import ReviewAudio

@receiver(models.signals.post_delete, sender=ReviewAudio)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.audio_review:
        if os.path.isfile(instance.audio_review.path):
            os.remove()
