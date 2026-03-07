from django.contrib import admin
from .models import LoginAttempt
from .models import APIAccessLog
from .models import FriendRequest
@admin.register(LoginAttempt)
class LoginAttemptAdmin(admin.ModelAdmin):
    list_display = ('username', 'ip_address', 'success', 'timestamp')
    list_filter = ('success', 'timestamp')
    search_fields = ('username', 'ip_address')


@admin.register(APIAccessLog)
class APIAccessLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'ip_address', 'endpoint', 'method', 'response_status', 'timestamp')
    list_filter = ('method', 'response_status', 'timestamp')
    search_fields = ('user__username', 'ip_address', 'endpoint')
    readonly_fields = ('timestamp',)

@admin.register(FriendRequest)
class FriendRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'from_user', 'to_user', 'created_at', 'status')
    list_filter = ('status', 'created_at')
    search_fields = ('from_user__username', 'to_user__username')
    # list_editable = ('status',)
    readonly_fields = ('created_at',)