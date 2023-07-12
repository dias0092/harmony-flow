from django.urls import path
from . import views

urlpatterns = [
    path('', views.track_list, name='track_list'),
    path('<int:pk>/', views.track_detail, name='track_detail'),
    path('new/', views.track_new, name='track_new'),
    path('<int:pk>/edit/', views.track_edit, name='track_edit'),
    path('<int:pk>/delete/', views.track_delete, name='track_delete'),
]