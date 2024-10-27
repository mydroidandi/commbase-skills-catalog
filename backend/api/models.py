# Imports
from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")  # If the user gets deleted, the model removes all the user notes
    # "notes" is the field name we wanna put on the user that references all of
    # its notes. So from the User object I am able to access .notes, which will
    # give you all the note objects the User has created.

    def __str__(self):
        return self.title
