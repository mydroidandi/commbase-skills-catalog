# Imports
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note  # Import a model from models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]  # Model fields
        extra_kwargs = {"author": {"read_only": True}}  # Tell the serializer to manually set who the author is based on who created this note
        # You do not want someone to tell you who the author is
