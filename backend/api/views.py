
# from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer,NoteSerializer,FamilyDetailsSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note,User,FamilyDetails
from rest_framework.response import Response
from rest_framework import status


# Create your views here.


class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
    
    def perform_create(self,serializer):
        if serializer.is_valid():
            serializer.save(author= self.request.user)
        else:
            print(serializer.errors)

class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]



class FamilyDetailsListCreateView(generics.ListCreateAPIView):
    serializer_class = FamilyDetailsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return FamilyDetails.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author= self.request.user)
        else:
            print(serializer.errors)

    
class FamilyDetailsUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FamilyDetailsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return FamilyDetails.objects.filter(user=self.request.user)

