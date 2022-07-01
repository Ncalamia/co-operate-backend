from rest_framework import serializers
from .models import EmployeeItem


class EmployeeItemSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = EmployeeItem # tell django which model to use
        fields = ('id', 'name', 'item', 'event') # tell django which fields to include

