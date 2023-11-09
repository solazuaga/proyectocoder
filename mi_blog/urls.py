from operator import index
from re import search
from django.urls import path

from blog1.views import create_post

urlpatterns = [
    path('', index, name='index'),  
    path('create_post/', create_post, name='create_post'),
    path('search/', search, name='search'),
]
