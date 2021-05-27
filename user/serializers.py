from rest_framework import serializers

from .models import MaaliUser

class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=63, min_length=8, write_only=True)

    class Meta:
        model = MaaliUser
        fields = ('email', 'first_name', 'last_name', 'password')

    def create(self, validated_data):
        return MaaliUser.objects.create_user(**validated_data)

class LoginSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=63, min_length=8, write_only=True)

    class Meta:
        model = MaaliUser
        fields = ('email', 'first_name', 'last_name', 'password', 'token')

        read_only_fields = ['token']

class UserDetailsSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=63, min_length=8, write_only=True)

    class Meta:
        model = MaaliUser
        fields = ('email', 'first_name', 'last_name', 'password', 'joined', 'last_login')