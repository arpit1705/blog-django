from django.db import models
from django.urls import reverse

class Thing(models.Model):
	
	title= models.CharField(max_length=100)
	description= models.TextField(blank=True)
	priority= models.IntegerField()
	picture= models.ImageField(default='things/default.jpeg', upload_to='things')

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog-home')

class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title= models.CharField(max_length=200)
    genre= models.CharField(max_length=100)
    album_logo= models.ImageField(default='music/default.jpeg', upload_to='music')

    # def get_absolute_url(self):
        # return reverse('music:detail')

    def __str__(self):
        return self.album_title+ '-'+ self.artist

class Song(models.Model):
    album= models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title=models.CharField(max_length=250)

    def __str__(self):
        return self.song_title


