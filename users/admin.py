from django.contrib import admin
from .models import SoundHomeUsers, SoundHomeUsersAdditionalInfo, SoundHomeUsersWhatUsersLikes

# Register your models here.

admin.site.register(SoundHomeUsers)
admin.site.register(SoundHomeUsersAdditionalInfo)
admin.site.register(SoundHomeUsersWhatUsersLikes)
