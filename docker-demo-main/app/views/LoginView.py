from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from ..models import LoginAttempt
from ..utils import get_client_ip, is_ip_logged_in, set_ip_logged_in

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        ip = get_client_ip(request)
        if is_ip_logged_in(ip):
            return Response({"error": "You are already logged in"}, status=status.HTTP_403_FORBIDDEN)
        username = request.data.get('username')
        password = request.data.get('password')
        ip_address = request.META.get('REMOTE_ADDR')
        
        if not username:
            LoginAttempt.objects.create(
                ip_address=ip_address,
                success=False
            )
            return Response({'error': 'Username is required'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.filter(username=username).first()
        
        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            LoginAttempt.objects.create(
                user=user,
                username=username,
                ip_address=ip_address,
                success=True
            )
            set_ip_logged_in(ip)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            LoginAttempt.objects.create(
                username=username,
                ip_address=ip_address,
                success=False
            )
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)