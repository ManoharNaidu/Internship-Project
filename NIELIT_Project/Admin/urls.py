from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('Admin/',views.admin,name='admin'),
    path('aLogin/',views.adminlogin,name='adminlogin'),
    path('aRegister/',views.adminregister,name='adminregister'),
    path('employee/',views.employee,name='employee'),
    # path('employee/<str:name>',views.employeeLogged,name='employeeLogged'),
    # path('Admin/<str:name>',views.adminLogged,name='adminLogged'),
    # path('createEmployee',views.createEmployee,name='createEmployee'),
    # path('updateEmployee',views.updateEmployee,name='updateEmployee'),
    # path('deleteEmployee',views.deleteEmployee,name='deleteEmployee'),
    # path('searchEmployee',views.searchEmployee,name='searchEmployee'),
]