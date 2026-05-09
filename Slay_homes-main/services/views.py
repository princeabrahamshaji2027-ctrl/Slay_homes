from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import Appointment, Notification
from .forms import AppointmentForm, AdminStatusUpdateForm

def role_required(role):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            # Allow superusers and staff to access admin-role views
            if role == 'admin' and (request.user.is_superuser or request.user.is_staff):
                return view_func(request, *args, **kwargs)
            if hasattr(request.user, 'role') and request.user.role == role:
                return view_func(request, *args, **kwargs)
            else:
                messages.error(request, "Access denied for your role.")
                return redirect('login')
        return _wrapped_view
    return decorator

@login_required
@role_required('client')
def get_notifications(request):
    notifications = request.user.notifications.filter(is_read=False)
    data = [{
        'id': notif.id,
        'message': notif.message,
        'created_at': notif.created_at.strftime("%Y-%m-%d %H:%M")
    } for notif in notifications]
    return JsonResponse({'notifications': data})

@login_required
@role_required('client')
def mark_notification_read(request, notif_id):
    if request.method == 'POST':
        notif = get_object_or_404(Notification, id=notif_id, user=request.user)
        notif.is_read = True
        notif.save()
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'})

@login_required
@role_required('client')
def client_home(request):
    return render(request, 'client/home.html')

@login_required
@role_required('client')
def client_yours(request):
    if request.method == 'POST':
        appt_id = request.POST.get('appointment_id')
        if appt_id:
            appt = get_object_or_404(Appointment, pk=appt_id, client=request.user)
            if appt.status in ['pending', 'in_progress']:
                appt.status = 'cancelled'
                appt.save()
                messages.success(request, "Appointment cancelled.")
        return redirect('client:yours')
        
    appointments = Appointment.objects.filter(client=request.user).order_by('-service_date', '-service_time')
    return render(request, 'client/yours.html', {'appointments': appointments})

@login_required
@role_required('client')
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.client = request.user
            appointment.save()
            messages.success(request, "Your appointment is booked!")
            return redirect('client:home')
    else:
        form = AppointmentForm()
    return render(request, 'client/book_appointment.html', {'form': form})

@login_required
@role_required('admin')
def admin_home(request):
    pending_requests = Appointment.objects.filter(
        status__in=['pending', 'in_progress']
    ).select_related('client').order_by('service_date')
    completed_requests = Appointment.objects.filter(
        status='completed'
    ).select_related('client').order_by('-updated_at')
    
    return render(request, 'admin_panel/home.html', {
        'pending_requests': pending_requests,
        'completed_requests': completed_requests
    })

@login_required
@role_required('admin')
def request_detail(request, pk):
    appt = get_object_or_404(Appointment, pk=pk)
    
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'update_status':
            status_form = AdminStatusUpdateForm(request.POST, instance=appt)
            if status_form.is_valid():
                updated_appt = status_form.save()
                Notification.objects.create(
                    user=updated_appt.client,
                    appointment=updated_appt,
                    message=f"Your appointment status was changed to {updated_appt.get_status_display()}."
                )
                messages.success(request, "Status updated.")
                return redirect('admin_panel:request_detail', pk=pk)
        elif action == 'delete':
            appt.delete()
            messages.success(request, "Appointment deleted.")
            return redirect('admin_panel:home')
        elif action == 'edit':
            edit_form = AppointmentForm(request.POST, instance=appt)
            if edit_form.is_valid():
                edit_form.save()
                messages.success(request, "Changes saved.")
                return redirect('admin_panel:home')
    else:
        status_form = AdminStatusUpdateForm(instance=appt)
        edit_form = AppointmentForm(instance=appt)
        
    return render(request, 'admin_panel/request_detail.html', {
        'appt': appt,
        'status_form': status_form,
        'edit_form': edit_form,
    })
