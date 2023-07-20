from django.contrib import admin
from .models import UserConfirmation, User


class UserModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'phone_number']


admin.site.register(User, UserModelAdmin)
admin.site.register(UserConfirmation)
