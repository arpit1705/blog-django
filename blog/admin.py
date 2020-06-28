from django.contrib import admin
from .models import Thing, Album, Song

admin.site.register(Thing)
admin.site.register(Album)
admin.site.register(Song)