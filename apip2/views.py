from django.http import Http404
from django.shortcuts import render
from . models import *
from .serializers import *
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.exceptions import ValidationError

class DepartmentView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer




class TeacherView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer




class ClasView(generics.ListCreateAPIView):
    queryset = Clas.objects.all()
    serializer_class = ClasSerializer

class ClasDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clas.objects.all()
    serializer_class = ClasSerializer




class FloorView(generics.ListCreateAPIView):
    queryset = Floor.objects.all()
    serializer_class = FloorSerializer

class FloorDetailsView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Floor.objects.all()
    serializer_class = FloorSerializer



