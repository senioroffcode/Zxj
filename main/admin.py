from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import *


@admin.register(User)
class UserAdmin(UserAdmin):
    fieldssets = (
        (None, {"field": {"username", "password"}}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions"
             ),
            },
        ),
        (
            _("Extra"),
            {
                "fields":(
                    "phone",
                    "satus",
                    "region",
                ),
            },
        ),
        (_("Important dates "), {"fields": ("last_login", "date_joined")})
    )