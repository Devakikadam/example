from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from ..models import FriendRequest
from ..serializers import FriendRequestSerializer

User = get_user_model()

class PendingFriendRequestsView(generics.ListAPIView):
    serializer_class = FriendRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return FriendRequest.objects.filter((Q(to_user=user) | Q(from_user=user)) & Q(status='pending'))