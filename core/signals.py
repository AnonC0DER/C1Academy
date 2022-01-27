from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import Group
from Student.models import Student
from Teacher.models import Teacher
from core.models import Account
from Manager.models import Manager
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
            profile = Student.objects.create(
                user = user,
                username = user.username,
                email = user.email,
                first_name = user.first_name,
                last_name = user.last_name,
            )
            
            # Set user permissions
            group = Group.objects.get(name='Student')
            user.groups.add(group)

        elif user.user_post == 'teacher':
            # create profile
            profile = Teacher.objects.create(
                user = user,
                username = user.username,
                email = user.email,
                first_name = user.first_name,
                last_name = user.last_name,
            )
            # Set user permissions
            group = Group.objects.get(name='Teacher')
            user.groups.add(group)
        
        elif user.user_post == 'manager':
            # create profile
            profile = Manager.objects.create(
                user = user,
                username = user.username,
                email = user.email,
                first_name = user.first_name,
                last_name = user.last_name,
            )
            # Set user permissions
            group = Group.objects.get(name='Manager')
            user.groups.add(group)


# Delete account
# @receiver(post_delete, sender=Student)
def DeleteUserAcc(sender, instance, **kwargs):
    '''If admin delete the profile, this function will delete the user, too.'''
    
    try:
        user = instance.user
        user.delete()
    except:
        pass

post_delete.connect(DeleteUserAcc, sender=Student)
post_delete.connect(DeleteUserAcc, sender=Teacher)
post_delete.connect(DeleteUserAcc, sender=Manager)