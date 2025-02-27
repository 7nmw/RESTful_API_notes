from rest_framework import serializers
from .models import Notes
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class NotesSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author_name.username')

    class Meta:
        model = Notes
        fields = ['id', 'author_name', 'header', 'content']
