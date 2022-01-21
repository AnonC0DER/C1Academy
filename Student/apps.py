from django.apps import AppConfig


class StudentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Student'

    # Ready method : https://docs.djangoproject.com/en/4.0/ref/applications/#django.apps.AppConfig.ready
    def ready(self):
        import Student.signals
