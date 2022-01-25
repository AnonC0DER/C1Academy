import uuid
from django.db import models
from core.models import Account
from django.core.validators import RegexValidator
#################################################

class Teacher(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=75, null=True, blank=True) 
    first_name = models.CharField(max_length=75, null=True, blank=True) 
    last_name = models.CharField(max_length=75, null=True, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message='Phone number must be entered in the format: +98xxxxxxxxxx. Up to 15 numbers allowed.')
    phone_number = models.CharField(validators=[phone_regex], max_length=15)
    image = models.ImageField(upload_to='TeacherImages/', default='StudentImage/default.jpg')
    # class =
    last_login = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True ,primary_key=True, editable=False)

    # Return username
    def __str__(self):
        return self.username

    # We use this property in frontend instead of profile_image, so if user deleted image, it doesn't break page
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = '/images/TeacherImages/default.jpg'

        return url


class Classroom(models.Model):
    '''Student classroom model'''
    name = models.CharField(max_length=120)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True)
    class_hours = models.CharField(max_length=60, help_text='Set class hours -> 6:45PM - 8:00PM')
    # home_work = models.ManyToManyField('HomeworkTeacherCanAdd')
    # homework = models.ManyToManyField('HomeworkTeacherCanAdd')
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name


class HomeworkTeacherAdd(models.Model):
    '''Teachers can add homework for students'''
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title