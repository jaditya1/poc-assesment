from django.contrib import admin
from .models import Profile, UserActivity


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "phone_number",
        "address",
        "latitude",
        "longitute",
        "updated_at",
    )
    readonly_fields = ["updated_at", "user"]

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    # only logged in user can edit his/her profile
    def get_queryset(self, request):
        if request.user.is_superuser == False:
            return Profile.objects.filter(user=request.user)
        else:
            return Profile.objects.all()


admin.site.register(Profile, UserProfileAdmin)


class UserActivityAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "activity",
        "created_at"
    )
    readonly_fields = ["activity", "user", 'created_at']

    list_filter = [
        'user',
        'created_at',
        'activity'
        ]

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    # only logged in user can edit his/her profile
    def get_queryset(self, request):
        if request.user.is_superuser == False:
            return UserActivity.objects.filter(user=request.user)
        else:
            return UserActivity.objects.all()


admin.site.register(UserActivity, UserActivityAdmin)
