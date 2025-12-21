from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from ...models import *
from ...extras import *

class RegisterSerializer(serializers.ModelSerializer):
    """
    A serializer class for registering new users
    """
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True},
            #'password2': {'write_only': True},
        }

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')
        password = attrs.get('password', '')
        password2 = attrs.get('password2', '')

        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': 'Email is taken'})

        if CustomUser.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                {'email': 'Username is taken'})

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})

        # The below uses more security validators listed in settings.
        # Raises validation error if any one fails, or returns none.
        if validate_password(password) is None:
            return super().validate(attrs)

    def save(self):
        instance = self.Meta.model(
            email=self.validated_data['email'],
            username=self.validated_data['username']
        )
        password = self.validated_data['password']
        instance.set_password(password)  # hashing happens here.
        instance.save()
        return instance

class RegisterDoneSerializer(serializers.ModelSerializer):
    """
    A serializer class for setting user account active based on email registration link.
    """
    token = serializers.SerializerMethodField()

    def get_token(self, obj):
        return self.context.get('token')

    class Meta:
        model = CustomUser
        fields = ['token']

class LoginSerializer(serializers.Serializer):
    """
    A serializer class for logon.
    """
    username = serializers.CharField(max_length=255, min_length=1)
    password = serializers.CharField(max_length=68, min_length=1, write_only=True)
    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):
        user = CustomUser.objects.get(username=obj['username'])
        return get_tokens(user)

    class Meta:
        fields = ['username', 'password', 'tokens']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, attrs):

        username = attrs.get('username', '')
        password = attrs.get('password', '')
        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError('Invalid credentials, try again')
        elif not user.is_active:
            serializers.ValidationError('Account disabled, contact admin')
        else:
            return {
                'username': user.username,
                'tokens': user.tokens
            }
        return None

class LogoutSerializer(serializers.Serializer):
    """
    A serializer class for logout.
    """
    refresh = serializers.CharField()

    def validate(self, attrs):
        self.refresh = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.refresh).blacklist()

        except TokenError:
            raise AuthenticationFailed('Token error. May already be blacklisted.')

class ResetSerializer(serializers.ModelSerializer):
    """
    A serializer class for requesting a password reset email.
    """
    # email = serializers.EmailField(min_length=2)

    class Meta:
        model = CustomUser
        fields = ['email']

class ResetDoneSerializer(serializers.Serializer):
    """
    A serializer class for authenticating user based on email registration link.
    """
    #id = serializers.UUIDField(read_only=True)
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

    def validate(self, attrs):
        #id = attrs.get('id')
        password = attrs.get('password', '')
        password2 = attrs.get('password2', '')

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})

        # uses validators listed in settings. Raises validation error if any one fails, or returns none.
        if validate_password(password) is None:
            return super().validate(attrs)


    def update_password(self):
        password = self.validated_data['password']
        real_user = self.user
        real_user.set_password(password)  # hashing happens here.
        real_user.save()


class BasicUserSerializer(serializers.ModelSerializer):
    """
    A serializer class for providing basic user info for internal use on the front end.
    """
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'about', 'is_staff']

class EditUserSerializer(serializers.ModelSerializer):
    """
    A serializer class for users to edit their profile.
    """
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'about', 'picture', 'password']
        extra_kwargs = {
            'id': {'read_only': True},
            'password': {'write_only': True}
        }

class PromoteUserSerializer(serializers.ModelSerializer):
    """
    A serializer class for curators to recruit new curators.
    """
    class Meta:
        model = CustomUser
        fields = [ 'username', 'is_staff']
        extra_kwargs = {
            'username': {'read_only': True},
        }

