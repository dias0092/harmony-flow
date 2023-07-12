from django.urls import path
from .views import artist_list, artist_detail, artist_new, artist_edit, artist_delete

app_name='artists'

urlpatterns = [
    path('artists/', artist_list, name='artist_list'),
    path('artist/<int:pk>/', artist_detail, name='artist_detail'),
    path('artist/new/', artist_new, name='artist_new'),
    path('artist/<int:pk>/edit/', artist_edit, name='artist_edit'),
    path('artist/<int:pk>/delete/', artist_delete, name='artist_delete'),
]