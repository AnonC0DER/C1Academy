from rest_framework import generics
from API.serializers import AccountSerializer


class CreateAccountView(generics.CreateAPIView):
    '''Create a new account'''
    serializer_class = AccountSerializer