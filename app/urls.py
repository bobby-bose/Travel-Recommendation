# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('password_recovery/', views.password_recovery, name='password_recovery'),
    path('travel_preferences/', views.travel_preferences, name='travel_preferences'),
]