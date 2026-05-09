from django.urls import path
from . import views

app_name = 'admin_panel'

urlpatterns = [
    path('home/', views.admin_home, name='home'),
    path('request/<int:pk>/', views.request_detail, name='request_detail'),
]
