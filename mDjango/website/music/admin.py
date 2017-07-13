from django.contrib import admin
from .models import Album, Song

# Music app admin.py file
# Register your models here.

admin.site.register(Album)
admin.site.register(Song)
