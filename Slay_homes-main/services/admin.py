from django.contrib import admin
from .models import Appointment

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['client', 'phone_number', 'service_date', 'service_time', 'status', 'created_at']
    list_filter = ['status', 'service_date']
    search_fields = ['client__username', 'phone_number', 'address']

admin.site.register(Appointment, AppointmentAdmin)
