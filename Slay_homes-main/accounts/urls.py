from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('clear-animation-flag/', views.clear_animation_flag, name='clear_animation_flag'),
]
