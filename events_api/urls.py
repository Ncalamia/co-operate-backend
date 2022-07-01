from django.urls import path
from . import views

urlpatterns = [
    path('api/events', views.EventList.as_view(), name='event_list'), # api/events will be routed to the EventList view for handling
    path('api/events/<int:pk>', views.EventDetail.as_view(), name='event_detail'), # api/events will be routed to the EventDetail view for handling
]
