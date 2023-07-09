from django.urls import path
from .views import playlist_list, playlist_detail, playlist_new, playlist_edit, playlist_delete

urlpatterns = [
    path('playlists/', playlist_list, name='playlist_list'),
    path('playlist/<int:pk>/', playlist_detail, name='playlist_detail'),
    path('playlist/new/', playlist_new, name='playlist_new'),
    path('playlist/<int:pk>/edit/', playlist_edit, name='playlist_edit'),
    path('playlist/<int:pk>/delete/', playlist_delete, name='playlist_delete'),
]