from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import EmployeeSerializer
from .models import Employee

class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = EmployeeSerializer # tell django what serializer to use

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all().order_by('id')
    serializer_class = EmployeeSerializer
