from django.urls import path

from new_artists.views import *

urlpatterns = [
    path('new_artists/', index),
]