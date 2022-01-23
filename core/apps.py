from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

     # Ready method : https://docs.djangoproject.com/en/4.0/ref/applications/#django.apps.AppConfig.ready
    def ready(self):
        import core.signals