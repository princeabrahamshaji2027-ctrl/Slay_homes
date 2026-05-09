from django.db import models
from django.conf import settings

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('pending',     'Pending'),
        ('in_progress', 'In Progress'),
        ('completed',   'Completed'),
        ('cancelled',   'Cancelled'),
    ]

    client        = models.ForeignKey(
                        settings.AUTH_USER_MODEL,
                        on_delete=models.CASCADE,
                        related_name='appointments'
                    )
    phone_number  = models.CharField(max_length=20)
    address       = models.TextField()
    service_date  = models.DateField(db_index=True)
    service_time  = models.TimeField()
    description   = models.TextField(
                        help_text="Describe the service needed (renovation, cleaning, etc.)"
                    )
    status        = models.CharField(
                        max_length=20,
                        choices=STATUS_CHOICES,
                        default='pending',
                        db_index=True
                    )

    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['service_date', 'service_time']

    def __str__(self):
        return f"{self.client.get_full_name()} — {self.service_date} ({self.status})"

class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Notification for {self.user.username}"
