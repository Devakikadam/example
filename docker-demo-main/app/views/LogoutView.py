from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken

from ..models import BlacklistedToken
from ..utils import get_client_ip, clear_ip_logged_in

        
class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh_token")
            if not refresh_token:
                return Response({"error": "Refresh token is required"}, status=status.HTTP_400_BAD_REQUEST)
            
            try:
                token = RefreshToken(refresh_token)
            except TokenError:
                return Response({"error": "Invalid refresh token"}, status=status.HTTP_400_BAD_REQUEST)
            
            # Check if token is already blacklisted
            jti = token.payload['jti']
            token_obj = OutstandingToken.objects.filter(token=str(refresh_token)).first()
            
            if not token_obj:
                return Response({"error": "Token not found"}, status=status.HTTP_404_NOT_FOUND)

            if BlacklistedToken.objects.filter(token=token_obj).exists():
                return Response({"error": "Token is already blacklisted"}, status=status.HTTP_400_BAD_REQUEST)

            # Blacklist the token
            BlacklistedToken.objects.create(token=token_obj)
            
            ip = get_client_ip(request)
            clear_ip_logged_in(ip)

            return Response({"success": "Successfully logged out."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": f"Unexpected error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)