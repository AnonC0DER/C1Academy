from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from .models import *
from django.contrib import admin
#####################

class UserAdminConfig(UserAdmin):
    '''User'''
    ordering = ['-date_joined']
    list_display = ['email', 'username', 'first_name', 'last_name', 'user_post']
    # Ref : https://docs.djangoproject.com/en/4.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.search_fields
    search_fields = ['email', 'username', 'first_name', 'last_name']
    readonly_fields = ['date_joined', 'last_login']
    # define the sections
    # each one of these brackets are a section
    fieldsets = (
        # None is title for the section
        (None, {'fields' : ('email', 'password')}),
        (_('Personal info'), {'fields' : ('username', 'first_name', 'last_name')}),
        (_('Activity'), {'fields' : ('date_joined', 'last_login')}),
        (_('Permissions'), {'fields' : ('is_admin', 'is_active', 'is_staff', 'is_superuser')})
    )

    add_fieldsets = (
        (None, {
            'classes' : ('wide',),
            'fields' : ('email', 'username', 'first_name', 'last_name', 'user_post', 'password1', 'password2'),
        }),
    )

admin.site.register(Account, UserAdminConfig)