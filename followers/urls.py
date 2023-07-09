from django.urls import path
from . import views

urlpatterns = [
    path('', views.follower_list, name='follower_list'),
    path('follower/<int:pk>/', views.follower_detail, name='follower_detail'),
    path('follower/new/', views.follower_new, name='follower_new'),
    path('follower/<int:pk>/edit/', views.follower_edit, name='follower_edit'),
    path('follower/<int:pk>/delete/', views.follower_delete, name='follower_delete'),
]