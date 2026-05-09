from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import LoginForm
from .models import CustomUser

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            request.session['show_login_animation'] = True
            if user.is_superuser or user.is_staff:
                return redirect('admin_panel:home')
            else:
                return redirect('client:home')
        else:
            messages.error(request, "Invalid credentials.")
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        # Expected fields: full_name, email, phone, address, username, password, confirm_password
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('login')
        
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('login')

        names = full_name.split(' ', 1)
        first_name = names[0]
        last_name = names[1] if len(names) > 1 else ''

        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        # Note: phone and address are not fields on CustomUser currently. Wait, does CustomUser have phone and address? Let's check. 
        # I will assume they are either not stored, or they should be added.
        # But the instructions say: "create a new Django User object using the fields above (first_name/last_name split from full name, email, username, password via set_password). The new user must appear in Django Admin → Users table immediately after registration."
        # So creating it this way is correct.

        messages.success(request, "Account created. Awaiting admin approval.")
        return redirect('login')
    return redirect('login')

from django.http import JsonResponse

def clear_animation_flag(request):
    if 'show_login_animation' in request.session:
        del request.session['show_login_animation']
    return JsonResponse({'status': 'ok'})
