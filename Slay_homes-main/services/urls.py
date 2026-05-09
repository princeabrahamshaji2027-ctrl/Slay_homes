from django.urls import path
from . import views

app_name = 'services' # Namespace handled in main urls.py but good practice to define app_name
# Wait, the instruction says to include with namespace, so app_name is required here.

urlpatterns = [
    # Paths will be prefixed in main urls.py
    path('home/', views.client_home, name='home'),
    path('book/', views.book_appointment, name='book_appointment'),
    path('request/<int:pk>/', views.request_detail, name='request_detail'),
]
