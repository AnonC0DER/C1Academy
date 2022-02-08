from rest_framework import generics
from API.serializers import AccountSerializer, AuthTokenSerializer
from rest_framework.settings import api_settings
from rest_framework.authtoken.views import ObtainAuthToken


class CreateAccountView(generics.CreateAPIView):
    '''Create a new account'''
    serializer_class = AccountSerializer


class CreateTokenView(ObtainAuthToken):
    '''Create a new auth token for user'''
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES