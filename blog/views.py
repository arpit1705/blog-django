from django.shortcuts import render
from .models import Thing, Album, Song
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin



class ThingListView(ListView):
	model= Thing
	template_name= 'blog/home.html'
	ordering=['priority']
	paginate_by= 4

def about(request):
	return render(request, 'blog/about.html', {'title':'About'})


class ThingCreateView(LoginRequiredMixin, CreateView):
	model= Thing
	fields= ['title', 'description', 'priority', 'picture']

class AlbumListView(ListView):
	model= Album
	template_name= 'blog/music.html'
	ordering=['artist']
	paginate_by= 9

