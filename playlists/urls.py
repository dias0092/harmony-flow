from django.urls import path
from .views import playlist_list, playlist_detail, playlist_new, playlist_edit, playlist_delete

urlpatterns = [
    path('', playlist_list, name='playlist_list'),
    path('<int:pk>/', playlist_detail, name='playlist_detail'),
    path('new/', playlist_new, name='playlist_new'),
    path('<int:pk>/edit/', playlist_edit, name='playlist_edit'),
    path('<int:pk>/delete/', playlist_delete, name='playlist_delete'),
]