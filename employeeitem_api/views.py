from django.shortcuts import render
from rest_framework import generics
from .serializers import EmployeeItemSerializer
from .models import EmployeeItem


# Create your views here.

# /employeeitem POST, GET
class EmployeeItemList(generics.ListCreateAPIView):
    queryset = EmployeeItem.objects.all().order_by('id') 
    serializer_class = EmployeeItemSerializer 

# /employeeitem/:id
class EmployeeItemDetail(generics.RetrieveUpdateDestroyAPIView):
     queryset = EmployeeItem.objects.all().order_by('id')
     serializer_class = EmployeeItemSerializer

