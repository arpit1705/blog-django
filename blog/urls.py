from django.urls import path
from . import views
from .views import ThingListView, ThingCreateView, AlbumListView

urlpatterns = [
     path('', ThingListView.as_view(), name='blog-home'),
     path('music/', AlbumListView.as_view(), name='blog-music'),
     path('add/', ThingCreateView.as_view(), name='add-thing'),
     path('about/', views.about, name='blog-about'),

]