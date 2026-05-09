from functools import wraps

from django.contrib import messages
from django.shortcuts import redirect


def role_required(role):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if getattr(request.user, "role", None) != role:
                messages.error(request, "Access denied for your role.")
                return redirect("login")
            return view_func(request, *args, **kwargs)

        return _wrapped_view

    return decorator
