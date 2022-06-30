from django.urls import path
from . import views

urlpatterns = [
    path('api/employees', views.EmployeeList.as_view(), name='employee_list',), 
    path('api/employees/<int:pk>', views.EmployeeDetail.as_view(), name='employee_detail',),
]
