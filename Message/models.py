import uuid
from django.db import models
from Student.models import Student
from Teacher.models import Teacher
from Manager.models import Manager
from core.models import Account
##################################

class MessageToStudent(models.Model):
    '''Teacher can Send message to student'''
    sender = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)
    recipient = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=200)
    message = models.TextField(null=True, blank=True) 
    is_read = models.BooleanField(default=False, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['is_read', '-created']


class ManagerToUser(models.Model):
    '''Manager can send message to all users'''
    sender = models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True, blank=True)
    recipient = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=200)
    message = models.TextField(null=True, blank=True) 
    is_read = models.BooleanField(default=False, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['is_read', '-created']