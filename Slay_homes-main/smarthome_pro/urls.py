from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.db import connections
from django.db.utils import OperationalError

def health_check(request):
    db_conn = connections['default']
    try:
        db_conn.cursor()
    except OperationalError:
        return JsonResponse({'status': 'unhealthy', 'database': 'disconnected'}, status=503)
    else:
        return JsonResponse({'status': 'healthy', 'database': 'connected'})

urlpatterns = [
    path('health/', health_check),
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('client/', include('services.client_urls', namespace='client')),
    path('admin-panel/', include('services.admin_urls', namespace='admin_panel')),
]

