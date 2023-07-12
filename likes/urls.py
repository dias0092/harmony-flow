from django.urls import path
from . import views

urlpatterns = [
    path('', views.like_list, name='like_list'),
    path('<int:pk>/', views.like_detail, name='like_detail'),
    path('new/', views.like_new, name='like_new'),
    path('<int:pk>/edit/', views.like_edit, name='like_edit'),
    path('<int:pk>/delete/', views.like_delete, name='like_delete'),
]