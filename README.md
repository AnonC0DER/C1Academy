# C1Academy

## Summary
This project is an open-source academy management system. It can be used for schools, too.
There are four types of users, Superuser, Manager, Teacher and student.
Manager must be able to send message to all users. Teacher must be able to send a message to students. 
And students can view their messages.

**_Give me a hand with front-end_**


## Plans
- [ ] Use a front-end template
- [x] Rest APIs


# Setting up things

## Environment
Create a file named `.env` in the root directory and add all the variables there. An example of `.env` file:
```
HOST=localhost
DATABASE=test
USERNAME=testuser
PASSWORD=testpass123
ESQL_TOKEN=xxxxxxxxxxxxxxxx
```

## Commands
1. `python manage.py migrate`
2. `python manage.py create_groups`
3. `python manage.py createsuperuser`

In step 2, this custom management command create custom groups with custom permissions. <br>
So, users will add to these groups, and they can have different permissions.


## Custom management commands
I used [ElephantSQL](https://elephantsql.com/) database, so I created some custom management commands for myself <br>
to make it easier to interact to ESQL database APIs. If you're using this database for your own database. <br>
So, these commands can help you too :
- `python manage.py backups` -> List of all backups
- `python manage.py create` -> Create a new backup
- `python manage.py restore` -> Restore a backup using its ID


## Files
- [Custom user model](https://github.com/AnonC0DER/C1Academy/blob/main/core/models.py)
- [Unit tests](https://github.com/AnonC0DER/C1Academy/tree/main/core/tests)
- [Custom management commands](https://github.com/AnonC0DER/C1Academy/tree/main/core/management)
- [Project Preview](https://github.com/AnonC0DER/C1Academy/tree/main/ProjectPreview)
- [Message model](https://github.com/AnonC0DER/C1Academy/tree/main/Message)
- [Manager model](https://github.com/AnonC0DER/C1Academy/tree/main/Manager)
- [Teacher model](https://github.com/AnonC0DER/C1Academy/tree/main/Teacher)
- [Student model](https://github.com/AnonC0DER/C1Academy/tree/main/Student)
- [Static files](https://github.com/AnonC0DER/C1Academy/tree/main/static)
