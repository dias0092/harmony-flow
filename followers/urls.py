from django.urls import path
from . import views

app_name='followers'

urlpatterns = [
    path('', views.follower_list, name='follower_list'),
    path('<int:pk>/', views.follower_detail, name='follower_detail'),
    path('new/', views.follower_new, name='follower_new'),
    path('<int:pk>/edit/', views.follower_edit, name='follower_edit'),
    path('<int:pk>/delete/', views.follower_delete, name='follower_delete'),
]