from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.core.cache import cache
from ..models import FriendRequest
from ..serializers import FriendRequestSerializer

User = get_user_model()

class SendFriendRequestView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        to_user_id = request.data.get('to_user')
        to_user = get_object_or_404(User, id=to_user_id)

        # Rate limiting
        cache_key = f"friend_requests_{request.user.id}"
        requests_made = cache.get(cache_key, 0)
        if requests_made >= 3:
            return Response({"error": "Rate limit exceeded. Try again later."}, status=status.HTTP_429_TOO_MANY_REQUESTS)

        friend_request, created = FriendRequest.objects.get_or_create(
            from_user=request.user,
            to_user=to_user,
            defaults={'status': 'pending'}
        )

        if not created:
            return Response({"error": "Friend request already sent."}, status=status.HTTP_400_BAD_REQUEST)

        # Update rate limit
        cache.set(cache_key, requests_made + 1, 60)  # 60 seconds expiry

        return Response(FriendRequestSerializer(friend_request).data, status=status.HTTP_201_CREATED)