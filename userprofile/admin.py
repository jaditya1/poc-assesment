from django.contrib import admin
from .models import Profile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'address', 'latitude', 'longitute', 'updated_at')
    readonly_fields = ['updated_at','user']

    # only logged in user can edit his/her profile
    def get_queryset (self, request):
       return Profile.objects.filter(user = request.user)

admin.site.register(Profile, UserProfileAdmin)