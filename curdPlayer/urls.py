from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('addPlayer/',AddPlayer.as_view(),name='addPlayer'),
    path('deletePlayer/',DeletePlayer.as_view(),name='deletePlayer'),
    path('updatePlayer/<int:id>/',UpdatePlayer.as_view(),name='updatePlayer'),
]
