from django.core.cache import cache
from django.utils import timezone
from datetime import timedelta

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def is_ip_logged_in(ip):
    return cache.get(f'logged_in_{ip}', False)

def set_ip_logged_in(ip, logged_in=True):
    cache.set(f'logged_in_{ip}', logged_in, timeout=24*60*60)  # 24 hours

def clear_ip_logged_in(ip):
    cache.delete(f'logged_in_{ip}')