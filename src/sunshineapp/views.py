from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework import viewsets
from sunshineapp.serializers import UserSerializer
from rest_framework.permissions import(
    IsAdminUser,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly
)
from .permissions import IsOwnerOrReadOnly
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
   
    permission_classes=[IsOwnerOrReadOnly,IsAuthenticatedOrReadOnly]

