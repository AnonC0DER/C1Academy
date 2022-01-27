from django.core.management import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission

# Permission groups
GROUPS = {
    'Manager' : {
        'manager' : ['view', 'add'],
        'group' : ['view', 'add'],
        'manager to user' : ['view', 'add', 'change', 'delete'],
        'message to student' : ['view', 'add', 'change', 'delete'],
        'student' : ['view', 'add', 'change', 'delete'],
        'classroom' : ['view', 'add', 'change', 'delete'],
        'teacher' : ['view', 'add', 'change', 'delete'],
    },

    'Teacher' : {
        'message to student' : ['view', 'add', 'change', 'delete'],
        'classroom' : ['view', 'add', 'change', 'delete'],
        'homework teacher add' : ['view', 'add', 'change', 'delete'],
        'learning content' : ['view', 'add', 'change', 'delete'],
        'teacher' : ['view'],
    },

    'Student' : {
        'message to student' : ['view'],
        'learning content' : ['view'],
        'homework student add' : ['view', 'add', 'change', 'delete'],
    }
}


class Command(BaseCommand):
    '''Create groups and permissions'''

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING('\nCreating groups, pleas wait...\n')) 
        
        # Loop group in groups
        for group in GROUPS:
            # Create new group by group name
            new_group, created = Group.objects.get_or_create(name=group)
            
            # Loop models in group
            for model in GROUPS[group]:

                # Loop permissions in group
                for permission_name in GROUPS[group][model]:
                    
                    # Create permission name
                    name = f'Can {permission_name} {model}'
                    self.stdout.write(self.style.SUCCESS(f'Creating {group} group, {name}...'))

                    try:
                        # Create the permission object
                        model_add_perm = Permission.objects.get(name=name)
                    except Exception as e:
                        self.stdout.write(self.style.NOTICE(f'\nSomething went wrong !\nError : {e}'))
                        break
                    
                    # Add permission object to group
                    new_group.permissions.add(model_add_perm)
        
        self.stdout.write('\nDone !')