from django.urls import path
from . import views

urlpatterns = [
    path('', views.usersong_list, name='usersong_list'),
    path('<int:pk>/', views.usersong_detail, name='usersong_detail'),
    path('new/', views.usersong_new, name='usersong_new'),
    path('<int:pk>/edit/', views.usersong_edit, name='usersong_edit'),
    path('<int:pk>/delete/', views.usersong_delete, name='usersong_delete'),
]