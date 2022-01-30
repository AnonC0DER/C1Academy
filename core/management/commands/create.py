from os import getenv, system
from django.core.management.base import BaseCommand
from requests import post
from dotenv import load_dotenv
load_dotenv()


class Command(BaseCommand):
    '''Create Backup command'''

    def handle(self, *args, **kwargs):
        '''Create a new backup from elephantsql database'''
        
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
            data = {
                'db' : DATABASE
            }
            auth = ('', ESQL_TOKEN)

            try:
                # Create request 
                req = post(url, data=data, auth=auth)
                # Check the status code
                if req.status_code == 200:
                    # Clear terminal
                    system('clear')
                    # print result
                    self.stdout.write(self.style.SUCCESS(f'Result :\n\n{req}\nBackup created successfully.'))

            except Exception as e:
                # print error
                self.stdout.write(self.style.ERROR(e))