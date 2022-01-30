from os import getenv, system
from django.core.management.base import BaseCommand
from requests import get
from dotenv import load_dotenv
load_dotenv()


class Command(BaseCommand):
    '''
    Backup list command

    Django command to get backup list
    
    The handle() method takes one or more poll_ids and sets poll.opened to False for each one. 
    If the user referenced any nonexistent polls, a CommandError is raised. 

    REF : https://docs.djangoproject.com/en/4.0/howto/custom-management-commands/
    
    These two *args, **options are allow us to passing in custom arguments
    and options to our management commands.
    
    We can print things out to the terminal using :
    self.stdout.write()

    We can use styles, too.
    self.stdout.write(self.style.SUCCESS('Database is ready !'))
    '''

    def handle(self, *args, **kwargs):
        '''List backups for last 30 days, ordered with the most recent first from elephantsql'''
        
        # Get values from .env file
        DATABASE = getenv('NAME')
        ESQL_TOKEN = getenv('ESQL_TOKEN')

        # Check values
        if DATABASE == None or ESQL_TOKEN == None or DATABASE == '' or ESQL_TOKEN == '':
            self.stdout.write(self.style.ERROR('\nCan not get values from .env !\nCompare your .env file with github repo example :\ngithub.com/AnonC0DER/C1Academy'))
        
        else:
            self.stdout.write(self.style.WARNING('\nOkay, pleas wait...\n'))
            
            # Parameters
            url = 'https://api.elephantsql.com/api/backup'
            params = (
                ('db', DATABASE),
            )
            auth = ('', ESQL_TOKEN)

            try:
                # Create request
                req = get(url, params=params, auth=auth)
                
                # Clear terminal
                system('clear')
                # print result
                self.stdout.write(self.style.SUCCESS(f'Result : \n\n{req.text}'))
            
            except Exception as e:
                # print error
                self.stdout.write(self.style.ERROR(e))                                          