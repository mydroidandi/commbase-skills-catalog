# Imports
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note  # Imported from backend/backend/models.py


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()  # List of all objects to look at to make sure we do not create an user that already exists
    serializer_class = UserSerializer  # Data to accept to make a new user, in this case a 'username' and a 'password'
    permission_classes = [AllowAny]  # Allow anyone to use this view to create a new user (rest_framework.permissions)


class NoteListCreate(generics.ListCreateAPIView):
    """
    View that will List all of the notes that the user has created, or it will create a note
    """
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]  # You cannot call this route unless you authenticated and you passed a valid JWT token.

    def get_queryset(self):
        """
        Lists all the user notes.
        """
        user = self.request.user  # Access the request object, that specifies the user
        return Note.objects.filter(author=user)  # Filter the notes by user

    def perform_create(self, serializer):
        """
        Creates a note.
        Notes:
        If you want some custom functionality, you need to override specific
        methods, as we do here with the create method. Refer to the Django
        documetation.
        """
        # If the serializer (NoteSerializer) is valid and passes with all of
        # its data
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)


class NoteDelete(generics.DestroyAPIView):
    """
    View that Deletes a note.
    """
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)

# Create more views here...
