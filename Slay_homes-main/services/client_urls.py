from django.urls import path
from . import views

app_name = 'client'

urlpatterns = [
    path('home/', views.client_home, name='home'),
    path('book/', views.book_appointment, name='book_appointment'),
    path('yours/', views.client_yours, name='yours'),
    path('notifications/', views.get_notifications, name='get_notifications'),
    path('notifications/<int:notif_id>/read/', views.mark_notification_read, name='mark_notification_read'),
]
