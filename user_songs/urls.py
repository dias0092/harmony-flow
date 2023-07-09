from django.urls import path
from . import views

urlpatterns = [
    path('', views.usersong_list, name='usersong_list'),
    path('usersong/<int:pk>/', views.usersong_detail, name='usersong_detail'),
    path('usersong/new/', views.usersong_new, name='usersong_new'),
    path('usersong/<int:pk>/edit/', views.usersong_edit, name='usersong_edit'),
    path('usersong/<int:pk>/delete/', views.usersong_delete, name='usersong_delete'),
]