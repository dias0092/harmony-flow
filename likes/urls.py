from django.urls import path
from . import views

urlpatterns = [
    path('', views.like_list, name='like_list'),
    path('like/<int:pk>/', views.like_detail, name='like_detail'),
    path('like/new/', views.like_new, name='like_new'),
    path('like/<int:pk>/edit/', views.like_edit, name='like_edit'),
    path('like/<int:pk>/delete/', views.like_delete, name='like_delete'),
]