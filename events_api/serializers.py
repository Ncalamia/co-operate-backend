from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Event # tell django which model to use
        fields = ('id', 'title', 'when', 'time', 'where', 'notes') # tell django which fields to include

