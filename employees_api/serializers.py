from rest_framework import serializers 
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Employee # tell django which model to use
        fields = ('id', 'name', 'image', 'item') # tell django which fields to include
