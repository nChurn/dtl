from django.contrib import admin
from django.contrib.auth import (
    admin as auth_admin,
    models as auth_models,
)

from .models import User, Group


class UserAdmin(auth_admin.UserAdmin):
    list_display = ('full_name', 'email', 'is_staff')
    search_fields = ('first_name', 'last_name', 'email')
    filter_horizontal = ('user_permissions', 'groups')
    list_display_links = ('full_name',)
    ordering = ('id',)
    list_filter = ()

    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name'),
        }),
        ('Credentials', {
            'fields': ('email', 'password'),
        }),
        ('Permissions', {
            'fields': ('is_staff', 'is_superuser', 'groups'),
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'password1', 'password2'),
        }),
    )

    def full_name(self, obj):
        return obj.get_full_name()


admin.site.unregister(auth_models.Group)
admin.site.register(User, UserAdmin)
admin.site.register(Group, auth_admin.GroupAdmin)
