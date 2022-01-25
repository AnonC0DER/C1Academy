from django.contrib import admin
from Message.models import ManagerToUser, MessageToStudent

admin.site.register(MessageToStudent)
admin.site.register(ManagerToUser)