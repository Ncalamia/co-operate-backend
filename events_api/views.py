from django.shortcuts import render
from rest_framework import generics
from .serializers import EventSerializer
from .models import Event


# Create your views here.

# /event POST, GET
class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all().order_by('id') 
    serializer_class = EventSerializer 

# /event/:id
class EventDetail(generics.RetrieveUpdateDestroyAPIView):
     queryset = Event.objects.all().order_by('id')
     serializer_class = EventSerializer

