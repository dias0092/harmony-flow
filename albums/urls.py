from django.urls import path
from .views import album_list, album_detail, album_new, album_edit, album_delete

app_name = 'albums'

urlpatterns = [
    path('', album_list, name='album_list'),
    path('<int:pk>/', album_detail, name='album_detail'),
    path('new/', album_new, name='album_new'),
    path('<int:pk>/edit/', album_edit, name='album_edit'),
    path('<int:pk>/delete/', album_delete, name='album_delete'),
    ]