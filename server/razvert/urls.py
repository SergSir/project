from django.urls import path

from . import views

urlpatterns = [
    path('', views.create_user, name='create_user'),
    path('random-user/', views.get_random_user, name='get_random_user'),
    path('saved-users/', views.get_saved_users, name='get_saved_users'),
    path('get-user/', views.get_user, name='get_user'),
]
