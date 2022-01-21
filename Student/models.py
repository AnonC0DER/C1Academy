import uuid
from django.db import models
from core.models import Account
from Teacher.models import Classroom
from django.core.validators import RegexValidator
################################################

class StudentProfile(models.Model):
    '''Student profile model'''
    user = models.OneToOneField(Account, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=75, null=True, blank=True) 
    first_name = models.CharField(max_length=75, null=True, blank=True) 
    last_name = models.CharField(max_length=75, null=True, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message='Phone number must be entered in the format: +98xxxxxxxxxx. Up to 15 numbers allowed.')
    phone_number = models.CharField(validators=[phone_regex], max_length=15)
    image = models.ImageField(upload_to='StudentImages/', default='StudentImage/default.jpg')
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    # created = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    # Return username
    def __str__(self):
        return self.username

    # We use this property in frontend instead of profile_image, so if user deleted image, it doesn't break page
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = '/images/StudentImages/default.jpg'

        return url