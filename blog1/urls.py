from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('create_post/', create_post, name='create post'),
    path('search/', search, name='search'),
]