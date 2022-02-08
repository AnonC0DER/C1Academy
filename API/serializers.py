from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _


class AccountSerializer(serializers.ModelSerializer):
    '''Serialize account objects'''

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password', 'first_name', 'last_name', 'user_post')
        extra_kwargs = {
            'password': {
                'write_only': True,
                 'min_length': 6
            }
        }

    def create(self, validated_data):
        '''Create a new user with encrypted password and return it'''
        return get_user_model().objects.create_user(**validated_data)
    
    def update(self, instance, validated_data):
        '''
        Update a user, setting the password correctly and return it
    
        pop function -> The reason we provide None is  with pop 
        function we must provide a default value.
        This function is very similar to get except after
        its retrieved password, it will remove it from 
        original dictionary.
    
        super() -> Will call the ModelSerializer update function, 
        it'll call the default one in our function
        '''
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class AuthTokenSerializer(serializers.Serializer):
    '''
    Serializer for the user authentication object
    
    trim_whitespace -> We use it because it's possible to have whitespace in your
    password, and by default the Django rest framework serializer will trim it off
    '''
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type' : 'password'},
        trim_whitespace=False
    )

    # This function is what is called when we validate our serializer
    # It check the inputs are all correct
    def validate(self, attrs):
        '''Validate and authenticate the user'''
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            # This is how we access the context of the request
            request=self.context.get('request'),
            username=email,
            password=password
        )

        # If the authentication fails :
        if not user:
            msg = _('Unable to authenticate with provided credentials !')
            raise serializers.ValidationError(msg, code='authentication')
        

        attrs['user'] = user
        return attrs