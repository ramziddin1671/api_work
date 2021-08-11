from django.shortcuts import render
import rest_framework.permissions
from .models import Group, Person
from .serializer import GroupSerializer, PersonSerializer
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

# First parol-login
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated



# Pagination
# class MemberPagination(PageNumberPagination):
#     page_size = 1


class GroupListView(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = LimitOffsetPagination
    # # First
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class GroupDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = LimitOffsetPagination
    # First
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class PersonListView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    pagination_class = LimitOffsetPagination
   # # First
   #  authentication_classes = [BasicAuthentication]
   #  permission_classes = [IsAuthenticated]


class PersonDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    pagination_class = LimitOffsetPagination
   # # First
   #  authentication_classes = [BasicAuthentication]
   #  permission_classes = [IsAuthenticated]