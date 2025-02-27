from rest_framework import generics, permissions
from . import serializers
from .models import Notes
from .permissions import IsOwnerOrReadOnly
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny

class RegisterView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny ]


class NotesList(generics.ListCreateAPIView):
    queryset = Notes.objects.all()
    serializer_class = serializers.NotesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notes.objects.filter(author_name=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author_name=self.request.user)


class NotesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notes.objects.all()
    serializer_class = serializers.NotesSerializer
    permission_classes = [permissions.IsAuthenticated,
                          IsOwnerOrReadOnly]

    def get_queryset(self):
        return Notes.objects.filter(author_name=self.request.user)