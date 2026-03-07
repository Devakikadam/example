from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from ..serializers import UserSerializer
from ..models import FriendRequest
from django.db.models import Q

User = get_user_model()

class FriendsListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(
            Q(sent_friend_requests__to_user=self.request.user, sent_friend_requests__status='approved') |
            Q(received_friend_requests__from_user=self.request.user, received_friend_requests__status='approved')
        ).distinct()