from django.urls import path
from .views.RegisterView import RegisterView
from .views.LoginView import LoginView
from .views.LogoutView import LogoutView
from .views.ExampleView import ExampleView
from .views.OtherView import OtherView
from .views.UserSearchView import UserSearchView
from .views.SendFriendRequestView import SendFriendRequestView
from .views.ApproveFriendRequestView import ApproveFriendRequestView
from .views.RejectFriendRequestView import RejectFriendRequestView
from .views.PendingFriendRequestsView import PendingFriendRequestsView
from .views.FriendsListView import FriendsListView
from .views.UserProfileView import UserProfileView

urlpatterns = [
        path('register/', RegisterView.as_view(), name='register'),
        path('login/', LoginView.as_view(), name='login'),
        path('logout/', LogoutView.as_view(), name='logout'),
        path('example/', ExampleView.as_view(), name='example'),
        path('other/', OtherView.as_view(), name='other'),
        path('search/', UserSearchView.as_view(), name='search'),
        path('send-request/', SendFriendRequestView.as_view(), name='send-friend-request'),
        path('approve-request/<int:pk>/', ApproveFriendRequestView.as_view(), name='approve-friend-request'),
        path('reject-request/<int:pk>/', RejectFriendRequestView.as_view(), name='reject-friend-request'),
        path('pending-requests/', PendingFriendRequestsView.as_view(), name='pending-friend-requests'),
        path('friends-list/', FriendsListView.as_view(), name='friends-list'),
        path('profile/', UserProfileView.as_view(), name='user-profile'),
]