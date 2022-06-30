from django.urls import path
from . import views

urlpatterns = [
    path('api/employees', views.EmployeeList.as_view(), name='employee_list'), # api/employees will be routed to the EmployeeList view for handling
    path('api/employees/<int:pk>', views.EmployeeDetail.as_view(), name='employee_detail'), # api/employees will be routed to the EmployeeDetail view for handling
]
