import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smarthome_pro.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Create Admin User
if not User.objects.filter(username='admin_test').exists():
    User.objects.create_superuser('admin_test', 'admin@example.com', 'Admin@123')
    print("Admin user created")
else:
    print("Admin user already exists")

# Create Normal User
if not User.objects.filter(username='user_test').exists():
    User.objects.create_user('user_test', 'user@example.com', 'User@123')
    print("Normal user created")
else:
    print("Normal user already exists")
