from django.urls import path
from . import views

urlpatterns = [
    path('api/employeeitems', views.EmployeeItemList.as_view(), name='employeeitem_list'), # api/employeeitems will be routed to the EmployeeItemList view for handling
    path('api/employeeitems/<int:pk>', views.EmployeeItemDetail.as_view(), name='employeeitem_detail'), # api/employeeitems will be routed to the EmployeeItemDetail view for handling
]
