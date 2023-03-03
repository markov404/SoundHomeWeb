from django.contrib import admin
from .models import SoundHomeUsers, SoundHomeUsersAdditionalInfo

# Register your models here.

admin.site.register(SoundHomeUsers)
admin.site.register(SoundHomeUsersAdditionalInfo)
