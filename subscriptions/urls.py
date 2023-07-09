from django.urls import path
from . import views

urlpatterns = [
    path('subscriptionplan/', views.subscriptionplan_list, name='subscriptionplan_list'),
    path('subscriptionplan/<int:pk>/', views.subscriptionplan_detail, name='subscriptionplan_detail'),
    path('subscriptionplan/new/', views.subscriptionplan_new, name='subscriptionplan_new'),
    path('subscriptionplan/<int:pk>/edit/', views.subscriptionplan_edit, name='subscriptionplan_edit'),
    path('subscriptionplan/<int:pk>/delete/', views.subscriptionplan_delete, name='subscriptionplan_delete'),

    path('usersubscription/', views.usersubscription_list, name='usersubscription_list'),
    path('usersubscription/<int:pk>/', views.usersubscription_detail, name='usersubscription_detail'),
    path('usersubscription/new/', views.usersubscription_new, name='usersubscription_new'),
    path('usersubscription/<int:pk>/edit/', views.usersubscription_edit, name='usersubscription_edit'),
    path('usersubscription/<int:pk>/delete/', views.usersubscription_delete, name='usersubscription_delete'),
]