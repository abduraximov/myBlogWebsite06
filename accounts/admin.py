from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CreationForm, ChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CreationForm
    form = ChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'first_name', 'last_name', 'age', 'address', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age', 'address')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age', 'address')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
