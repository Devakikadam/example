from .models import APIAccessLog
from .utils import get_client_ip
from django.urls import resolve

class APILoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        path = request.path_info
        if path.startswith('/api/'):
            # resolved = resolve(path)
            APIAccessLog.objects.create(
                user=request.user if request.user.is_authenticated else None,
                ip_address=get_client_ip(request),
                endpoint=request.path,
                method=request.method,
                response_status=response.status_code
            )
        
        return response