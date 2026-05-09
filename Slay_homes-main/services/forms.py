from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['phone_number', 'address', 'service_date', 'service_time', 'description']
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'w-full rounded-md border-outline-variant bg-surface-container-lowest p-3 text-body-md text-on-surface focus:border-primary focus:ring-1 focus:ring-primary', 'placeholder': '+1 (555) 000-0000'}),
            'address': forms.TextInput(attrs={'class': 'w-full rounded-md border-outline-variant bg-surface-container-lowest p-3 text-body-md text-on-surface focus:border-primary focus:ring-1 focus:ring-primary', 'placeholder': 'Enter full address'}),
            'service_date': forms.DateInput(attrs={'type': 'date', 'class': 'w-full rounded-md border-outline-variant bg-surface-container-lowest p-3 text-body-md text-on-surface focus:border-primary focus:ring-1 focus:ring-primary'}),
            'service_time': forms.TimeInput(attrs={'type': 'time', 'class': 'w-full rounded-md border-outline-variant bg-surface-container-lowest p-3 text-body-md text-on-surface focus:border-primary focus:ring-1 focus:ring-primary'}),
            'description': forms.Textarea(attrs={'rows': 5, 'class': 'w-full rounded-md border-outline-variant bg-surface-container-lowest p-3 text-body-md text-on-surface focus:border-primary focus:ring-1 focus:ring-primary', 'placeholder': 'e.g., Full house renovation, Deep cleaning, Waste removal...'}),
        }

class AdminStatusUpdateForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['status']
        widgets = {
            'status': forms.Select(attrs={'class': 'rounded-md border-outline-variant bg-surface-container-lowest p-2 text-body-md text-on-surface focus:border-primary focus:ring-1 focus:ring-primary'})
        }
