from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from ..models import FriendRequest

User = get_user_model()

class RejectFriendRequestView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        friend_request = get_object_or_404(FriendRequest, id=pk, to_user=request.user, status='pending')
        friend_request.status = 'rejected'
        friend_request.save()
        return Response({"message": "Friend request rejected."})