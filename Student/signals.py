from django.db.models.signals import post_save, post_delete
from Student.models import StudentProfile
from Teacher.models import Teacher
from core.models import Account
from django.dispatch import receiver
####################################

# Create profile
@receiver(post_save, sender=Account)
def CreateUserProfile(sender, instance, created, **kwargs):
    '''This function create a profile immediately after the user is generated'''

    if created:
        user = instance
        # Check user post
        if user.user_post == 'student':
            # create profile
            profile = StudentProfile.objects.create(
                user = user,
                username = user.username,
                email = user.email,
                first_name = user.first_name,
                last_name = user.last_name,
            )

        elif user.user_post == 'teacher':
            # create profile
            profile = Teacher.objects.create(
                user = user,
                username = user.username,
                email = user.email,
                first_name = user.first_name,
                last_name = user.last_name,
            )


# Delete account
@receiver(post_delete, sender=StudentProfile)
def DeleteUserAcc(sender, instance, **kwargs):
    '''If admin delete the profile, this function will delete the user, too.'''
    
    try:
        user = instance.user
        user.delete()
    except:
        pass