from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
# To make our application to support multiple languages, this function make things much easier
from django.utils.translation import gettext_lazy as _
##################################################

class AccountManager(BaseUserManager):
    '''Overwrite some functions in base user manager to handle our email address instead of the username'''
    
    def create_user(self, email, username, first_name, last_name, user_post, password, **extra_fields):
        '''Create and save a new user'''
        # If the email section is empty, raise an error
        if not email:
            raise ValueError(_('Users must have an email address !'))
        
        # If the username is already used, raise an error
        if not username:
            raise ValueError(_('Users must have an unique username !'))

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, first_name=first_name, last_name=last_name, user_post=user_post, **extra_fields)
        # set_password() -> Because of password hashing we use this helper function
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, first_name, last_name, user_post, password, **extra_fields):
        '''Create and save a new superuser'''

        # Get attrs from extra_fields and set default 
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('is_staff is set to False')
        
        elif extra_fields.get('is_superuser') is not True:
            raise ValueError('is_superuser is set to False')
        
        elif user_post != 'superuser':
            raise ValueError('User post is not superuser')

 
        # Create superuser
        return self.create_user(email, username, first_name, last_name, user_post, password, **extra_fields)


class Account(AbstractBaseUser, PermissionsMixin):
    '''Custom user model that support using email instead of username'''

    class UserPosts(models.TextChoices):
        SUPERUSER = 'superuser', _('Superuser')
        MANAGER = 'manager', _('Manager')
        TEACHER = 'teacher', _('Teacher')
        STUDENT = 'student', _('Student')
    
    email = models.EmailField(_('Email address'), max_length=255, unique=True)
    username = models.CharField(max_length=75, unique=True)
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    user_post = models.CharField(choices=UserPosts.choices, max_length=75, default=None)
    date_joined = models.DateField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = AccountManager()
    # We want to use email instead of user name, so change username field to email
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'user_post']

    def __str__(self):
        return self.email