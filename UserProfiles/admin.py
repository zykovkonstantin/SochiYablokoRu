from django.contrib import admin
from .models import UserProfile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class UserInline(admin.TabularInline):
    model = UserProfile
    can_delete = False
    verbose_name = 'Дополнительная информация'


class NewUserAdmin(UserAdmin):
    inlines = [UserInline, ]


admin.site.unregister(User)
admin.site.register(User, NewUserAdmin)
